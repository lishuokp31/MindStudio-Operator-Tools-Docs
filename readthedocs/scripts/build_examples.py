"""Examples page generation for MindStudio Operator Tools documentation.

Generates a hierarchical page tree under docs/examples/ mirroring the
examples/ source directory structure (tool -> category -> sample).
"""

from __future__ import annotations

import re
import shutil
import zipfile
from pathlib import Path
from typing import Callable


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------


def generate_examples_page(
    *,
    tools: list[dict],
    root: Path,
    docs_root: Path,
    repo_web_base_fn: Callable[[Path], str],
    first_heading_fn: Callable[[Path], str],
) -> None:
    """扫描 examples/ 目录，按 工具→分类→样例 的层级结构生成文档页面。

    Parameters
    ----------
    tools : list[dict]
        工具配置列表（TOOLS），每项需含 slug / title / branch / repo 字段。
    root : Path
        仓库根目录（ROOT）。
    docs_root : Path
        MkDocs docs 目录（DOCS_ROOT）。
    repo_web_base_fn : (Path) -> str
        根据子模块路径返回仓库主页 URL。
    first_heading_fn : (Path) -> str
        读取 Markdown 文件的首个标题。
    """
    # ---- 先清理旧生成内容（无论有无新样例） ----
    examples_docs_root = docs_root / "examples"
    if examples_docs_root.exists():
        shutil.rmtree(examples_docs_root)

    examples_source = root / "examples"
    if not examples_source.is_dir():
        print("[examples] examples 目录不存在，跳过生成。")
        return

    # 收集所有有样例的工具信息
    tool_entries: list[dict] = []
    for tool in tools:
        slug = tool["slug"]
        categories = _scan_examples(examples_source, slug, first_heading_fn)
        if not categories:
            continue
        tool_entries.append({
            "slug": slug,
            "title": tool["title"],
            "branch": tool["branch"],
            "repo_url": repo_web_base_fn(tool["repo"]),
            "categories": categories,
        })

    if not tool_entries:
        print("[examples] 未发现任何样例，跳过生成。")
        return

    examples_docs_root.mkdir(parents=True, exist_ok=True)

    # ---- 逐工具、逐分类、逐样例生成页面 ----
    for entry in tool_entries:
        slug = entry["slug"]
        title = entry["title"]
        branch = entry["branch"]
        repo_url = entry["repo_url"]
        categories = entry["categories"]

        tool_output_dir = examples_docs_root / slug

        # 工具级概览页
        _generate_tool_examples_overview_page(slug, title, repo_url, categories, tool_output_dir)

        for cat_name, samples in categories.items():
            cat_output_dir = tool_output_dir / cat_name

            # 分类级概览页
            _generate_category_overview_page(cat_name, samples, slug, cat_output_dir)

            for sample in samples:
                sample_output_dir = cat_output_dir / sample["name"]
                sample_output_dir.mkdir(parents=True, exist_ok=True)

                # 生成 source.zip 压缩包
                zip_path = sample_output_dir / "source.zip"
                _create_sample_zip(sample, zip_path)

                # 样例详情页
                _generate_sample_detail_page(sample, repo_url, branch, sample_output_dir)

    # ---- 顶层 examples/index.md（总览） ----
    overview_lines: list[str] = []
    overview_lines.append("# 算子工具使用样例")
    overview_lines.append("")
    overview_lines.append("本节汇集了各算子工具的使用样例，帮助开发者快速上手和理解工具的典型使用场景。")
    overview_lines.append("每个样例均包含完整的源码和说明文档，您可以直接下载并在本地环境运行。")
    overview_lines.append("")

    for entry in tool_entries:
        slug = entry["slug"]
        title = entry["title"]
        categories = entry["categories"]

        total_samples = sum(len(s) for s in categories.values())
        cat_count = len(categories)

        overview_lines.append(f"## [{title}]({slug}/)")
        overview_lines.append("")
        overview_lines.append(f"共 {cat_count} 个分类、{total_samples} 个样例。")
        overview_lines.append("")

        for cat_name, samples in categories.items():
            overview_lines.append(f"### {cat_name}")
            overview_lines.append("")
            for sample in samples:
                overview_lines.append(f"- **[{sample['display_name']}]({slug}/{cat_name}/{sample['name']}/)**")
                readme_text = sample["readme_path"].read_text(encoding="utf-8", errors="replace")
                first_para = _extract_first_paragraph(readme_text)
                if first_para:
                    short = first_para[:120].rsplit("。", 1)[0] + "。" if "。" in first_para[:120] else first_para[:120]
                    overview_lines.append(f"  {short}")
                overview_lines.append("")
            overview_lines.append("")

    (examples_docs_root / "index.md").write_text("\n".join(overview_lines), encoding="utf-8")

    # ---- 顶层 .nav.yml ----
    tool_slugs = [e["slug"] for e in tool_entries]
    nav_lines = ["title: 使用样例", "nav:", "  - index.md"]
    for ts in tool_slugs:
        nav_lines.append(f"  - {ts}")
    (examples_docs_root / ".nav.yml").write_text("\n".join(nav_lines) + "\n", encoding="utf-8")

    print(f"[examples] 样例页面已生成，涵盖工具: {', '.join(tool_slugs)}")


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _scan_examples(
    examples_root: Path,
    tool_slug: str,
    first_heading_fn: Callable[[Path], str],
) -> dict[str, list[dict]]:
    """扫描指定工具目录下的样例，返回 {分类目录名: [样例信息dict]} 的映射。"""
    tool_examples_dir = examples_root / tool_slug
    if not tool_examples_dir.is_dir():
        return {}

    result: dict[str, list[dict]] = {}
    for category_dir in sorted(tool_examples_dir.iterdir()):
        if not category_dir.is_dir():
            continue
        samples: list[dict] = []
        for sample_dir in sorted(category_dir.iterdir()):
            if not sample_dir.is_dir():
                continue
            readme = sample_dir / "README.md"
            if not readme.exists():
                continue
            source_files = sorted(
                [f for f in sample_dir.iterdir() if f.is_file() and f.name != "README.md"],
                key=lambda f: f.name,
            )
            display_name = first_heading_fn(readme)
            if not display_name or display_name == sample_dir.name:
                display_name = sample_dir.name.replace("_", " ").title()

            samples.append({
                "name": sample_dir.name,
                "display_name": display_name,
                "category": category_dir.name,
                "readme_path": readme,
                "source_files": source_files,
                "repo_rel_dir": f"examples/{tool_slug}/{category_dir.name}/{sample_dir.name}",
            })
        if samples:
            result[category_dir.name] = samples
    return result


def _create_sample_zip(sample: dict, output_path: Path) -> None:
    """将样例目录下的所有源文件（含 README）打包为 ZIP。"""
    sample_dir = sample["readme_path"].parent
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(sample_dir.iterdir()):
            if f.is_file():
                zf.write(f, f.name)


def _generate_sample_detail_page(
    sample: dict,
    tool_repo_url: str,
    tool_branch: str,
    output_dir: Path,
) -> None:
    """为单个样例生成详细页面（README 正文 + 一键压缩包下载）。

    压缩包在调用方已预先生成到 output_dir / "source.zip"。
    """
    readme_text = sample["readme_path"].read_text(encoding="utf-8", errors="replace")
    repo_rel_dir = sample["repo_rel_dir"]
    source_files = sample["source_files"]

    lines: list[str] = []
    lines.append(readme_text.rstrip())
    lines.append("")

    if source_files:
        file_list = " ".join(f"`{sf.name}`" for sf in source_files)
        lines.append("---")
        lines.append("")
        lines.append("## 📥 样例源码下载")
        lines.append("")
        lines.append("[📦 下载完整样例压缩包 :material-folder-zip-outline:](source.zip){ .md-button .md-button--primary }")
        lines.append("")
        lines.append(f"压缩包内包含以下文件：{file_list} `README.md`")
        lines.append("")

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")

    nav = ["nav:", "  - index.md"]
    (output_dir / ".nav.yml").write_text("\n".join(nav) + "\n", encoding="utf-8")


def _generate_category_overview_page(
    category_name: str,
    samples: list[dict],
    tool_slug: str,
    output_dir: Path,
) -> None:
    """为分类目录生成概览页面，列出该分类下所有样例。"""
    lines: list[str] = []
    lines.append(f"# {category_name}")
    lines.append("")
    lines.append(f"该分类包含以下 {len(samples)} 个样例：")
    lines.append("")

    for sample in samples:
        sample_slug = sample["name"]
        lines.append(f"### [{sample['display_name']}]({sample_slug}/)")
        lines.append("")
        readme_text = sample["readme_path"].read_text(encoding="utf-8", errors="replace")
        first_paragraph = _extract_first_paragraph(readme_text)
        if first_paragraph:
            lines.append(first_paragraph)
            lines.append("")

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")

    sub_items = [sample["name"] for sample in samples]
    nav_lines = ["nav:", "  - index.md"]
    for item in sub_items:
        nav_lines.append(f"  - {item}")
    (output_dir / ".nav.yml").write_text("\n".join(nav_lines) + "\n", encoding="utf-8")


def _generate_tool_examples_overview_page(
    tool_slug: str,
    tool_title: str,
    tool_repo_url: str,
    categories: dict[str, list[dict]],
    output_dir: Path,
) -> None:
    """为工具生成样例概览页面，列出该工具下所有分类及样例。"""
    lines: list[str] = []
    lines.append(f"# {tool_title} 使用样例")
    lines.append("")
    lines.append("该工具当前包含以下样例分类：")
    lines.append("")

    for cat_name, samples in categories.items():
        lines.append(f"## {cat_name}")
        lines.append("")
        for sample in samples:
            lines.append(f"- **[{sample['display_name']}]({cat_name}/{sample['name']}/)**")
            readme_text = sample["readme_path"].read_text(encoding="utf-8", errors="replace")
            first_paragraph = _extract_first_paragraph(readme_text)
            if first_paragraph:
                short = first_paragraph[:120].rsplit("。", 1)[0] + "。" if "。" in first_paragraph[:120] else first_paragraph[:120]
                lines.append(f"  {short}")
            lines.append("")

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")

    nav_lines = ["nav:", "  - index.md"]
    for cat_name in categories:
        nav_lines.append(f"  - {cat_name}")
    (output_dir / ".nav.yml").write_text("\n".join(nav_lines) + "\n", encoding="utf-8")


def _extract_first_paragraph(markdown_text: str) -> str:
    """从 Markdown 文本中提取第一个非标题、非空的有效段落。"""
    in_heading = True
    for line in markdown_text.splitlines():
        stripped = line.strip()
        if not stripped:
            in_heading = False
            continue
        if in_heading and stripped.startswith("#"):
            continue
        if stripped.startswith("#") or stripped.startswith("```") or stripped.startswith("---"):
            continue
        cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", stripped)
        cleaned = re.sub(r"[*_~`]", "", cleaned)
        cleaned = cleaned.strip()
        if cleaned and len(cleaned) > 5:
            return cleaned
    return ""
