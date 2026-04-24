from __future__ import annotations

import re
import shutil
import subprocess
import tarfile
import tempfile
import fnmatch
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS_ROOT = ROOT / "readthedocs" / "docs"


TOOLS = [
    {
        "slug": "msot",
        "title": "MindStudio Operator Tools",
        "branch": "master",
        "summary": "昇腾 AI 算子开发工具链",
        "repo": ROOT / "msot",
        "source_subdir": "docs/zh",
        "repo_readme": "README.md",
        "entry_points": [
            ("总体概览", "source/overview/overview.md"),
            ("快速入门", "source/quick_start/op_tool_quick_start.md"),
            ("安装指南", "source/install_guide/msot_install_guide.md"),
        ],
    },
    # {
    #     "slug": "mskpp",
    #     "title": "MindStudio Kernel Performance Prediction",
    #     "branch": "master",
    #     "summary": "昇腾 AI 算子设计工具",
    #     "repo": ROOT / "mskpp",
    #     "source_subdir": "docs/zh",
    #     "repo_readme": "README.md",
    #     "entry_points": [
    #         ("快速入门", "source/quick_start/mskpp_quick_start.md"),
    #         ("安装指南", "source/install_guide/mskpp_install_guide.md"),
    #         ("使用指南", "source/user_guide/mskpp_user_guide.md"),
    #         ("API参考", "source/api_reference/mskpp_api_reference.md"),
    #         ("架构设计说明书", "source/development_guide/architecture.md"),
    #         ("开发指南", "source/development_guide/develop_guide.md"),
    #     ],
    # },
    # {
    #     "slug": "msopgen",
    #     "title": "MindStudio Ops Generator",
    #     "branch": "master",
    #     "summary": "昇腾 AI 算子工程生成工具",
    #     "repo": ROOT / "msopgen",
    #     "source_subdir": "docs/zh",
    #     "repo_readme": "README.md",
    #     "entry_points": [
    #         ("快速入门", "source/quick_start/msopgen_quick_start.md"),
    #         ("安装指南", "source/install_guide/msopgen_install_guide.md"),
    #         ("使用指南", "source/user_guide/msopgen_user_guide.md"),
    #         ("典型案例", "source/best_practices/example.md"),
    #         ("架构设计说明书", "source/development_guide/architecture.md"),
    #         ("开发指南", "source/development_guide/develop_guide.md"),
    #     ],
    # },
    # {
    #     "slug": "mssanitizer",
    #     "title": "MindStudio Sanitizer",
    #     "branch": "master",
    #     "summary": "昇腾 AI 算子异常检测工具",
    #     "repo": ROOT / "mssanitizer",
    #     "source_subdir": "docs/zh",
    #     "repo_readme": "README.md",
    #     "entry_points": [
    #         ("快速入门", "source/quick_start/mssanitizer_quick_start.md"),
    #         ("安装指南", "source/install_guide/mssanitizer_install_guide.md"),
    #         ("使用指南", "source/user_guide/mssanitizer_user_guide.md"),
    #         ("典型案例", "source/best_practices/basic_cases.md"),
    #         ("API参考", "source/api_reference/mssanitizer_api_reference.md"),
    #         ("FAQ", "source/support/faq.md"),
    #         ("架构设计说明书", "source/development_guide/architecture.md"),
    #         ("开发指南", "source/development_guide/develop_guide.md"),
    #     ],
    # },
    # {
    #     "slug": "msdebug",
    #     "title": "MindStudio Debugger",
    #     "branch": "master",
    #     "summary": "昇腾 AI 算子调试工具",
    #     "repo": ROOT / "msdebug",
    #     "source_subdir": "docs/zh",
    #     "repo_readme": "README.md",
    #     "entry_points": [
    #         ("快速入门", "source/quick_start/msdebug_quick_start.md"),
    #         ("安装指南", "source/install_guide/msdebug_install_guide.md"),
    #         ("使用指南", "source/user_guide/msdebug_user_guide.md"),
    #         ("典型案例", "source/best_practices/basic_cases.md"),
    #         ("FAQ", "source/support/faq.md"),
    #         ("架构设计说明书", "source/development_guide/architecture.md"),
    #         ("开发指南", "source/development_guide/develop_guide.md"),
    #     ],
    # },
    # {
    #     "slug": "msopprof",
    #     "title": "MindStudio Ops Profiler",
    #     "branch": "master",
    #     "summary": "昇腾 AI 算子调优工具",
    #     "repo": ROOT / "msopprof",
    #     "source_subdir": "docs/zh",
    #     "repo_readme": "README.md",
    #     "entry_points": [
    #         ("快速入门", "source/quick_start/msopprof_quick_start.md"),
    #         ("安装指南", "source/install_guide/msopprof_install_guide.md"),
    #         ("使用指南", "source/user_guide/msopprof_user_guide.md"),
    #         ("典型案例", "source/best_practices/typical_cases.md"),
    #         ("架构设计说明书", "source/development_guide/architecture.md"),
    #         ("开发指南", "source/development_guide/develop_guide.md"),
    #     ],
    # },
    # {
    #     "slug": "msoptuner",
    #     "title": "MindStudio Ops Tuner",
    #     "branch": "master",
    #     "summary": "昇腾 AI 算子Tiling 参数寻优工具",
    #     "repo": ROOT / "msoptuner",
    #     "source_subdir": "docs/zh",
    #     "repo_readme": "README.md",
    #     "entry_points": [
    #         ("安装指南", "source/install_guide/msoptuner_install_guide.md"),
    #     ],
    # },
    # {
    #     "slug": "mskl",
    #     "title": "MindStudio Kernel Launcher",
    #     "branch": "master",
    #     "summary": "昇腾 AI 算子轻量化调用工具",
    #     "repo": ROOT / "mskl",
    #     "source_subdir": "docs/zh",
    #     "repo_readme": "README.md",
    #     "entry_points": [
    #         ("快速入门", "source/quick_start/mskl_quick_start.md"),
    #         ("安装指南", "source/install_guide/mskl_install_guide.md"),
    #         ("使用指南", "source/user_guide/mskl_user_guide.md"),
    #         ("API参考", "source/api_reference/mskl_api_reference.md"),
    #         ("FAQ", "source/support/faq.md"),
    #         ("开发指南", "source/development_guide/develop_guide.md"),
    #     ],
    # },
    # {
    #     "slug": "msopcom",
    #     "title": "MindStudio Ops Common",
    #     "branch": "master",
    #     "summary": "昇腾 AI 算子工具基础组件",
    #     "repo": ROOT / "msopcom",
    #     "source_subdir": "docs/zh",
    #     "repo_readme": "README.md",
    #     "entry_points": [
    #         ("安装指南", "source/development_guide/develop_guide.md"),
    #         ("架构设计说明书", "source/development_guide/architecture.md"),
    #         ("开发指南", "source/development_guide/develop_guide.md"),
    #     ],
    # },
    # {
    #     "slug": "mstx",
    #     "title": "MindStudio Tools Extension Library",
    #     "branch": "master",
    #     "summary": "昇腾 AI 算子工具扩展接口库",
    #     "repo": ROOT / "mstx",
    #     "source_subdir": "docs/zh",
    #     "repo_readme": "README.md",
    #     "entry_points": [
    #         ("安装指南", "source/install_guide/mstx_install_guide.md"),
    #         ("API参考", "source/api_reference/mstx_api_reference.md"),
    #         ("开发指南", "source/development_guide/develop_guide.md"),
    #     ],
    # },
]

EXCLUDED_NAMES = {
    "legal",
}

NON_NAV_NAMES = {
    "figures",
}

NAV_ORDER = [
    #  文件顺序
    "index.md",             # 首页
    "overview.md",          # 总体概览
    "*_quick_start.md",      # 快速入门
    "*_install_guide.md",    # 安装指南
    "*_user_guide.md",       # 使用指南
    "example.md",           # 典型案例
    "*_api_reference.md",    # API参考
    "faq.md",               # FAQ
    "architecture.md",      # 架构设计说明书
    "develop_guide.md",     # 开发指南

    # 目录顺序
    "overview",
    "quick_start",
    "install_guide",
    "user_guide",
    "best_practices",
    "api_reference",
    "support",
    "development_guide",
]

DISPLAY_DIR_WHITELIST = {
    "overview",
    "quick_start",
    "install_guide",
    "user_guide",
    "best_practices",
    "api_reference",
    "support",
    "development_guide",
    "figures"
}

DISPLAY_FILE_WHITELIST = {
    # "index.md",             # 首页
    # "overview.md",          # 总体概览
    # "*_quick_start.md",     # 快速入门
    # "*_install_guide.md",   # 安装指南
    # "*_user_guide.md",      # 使用指南
    # "example.md",           # 典型案例
    # "*_api_reference.md",   # API参考
    # "faq.md",               # FAQ
    # "architecture.md",      # 架构设计说明书
    # "develop_guide.md",     # 开发指南
}


def run_git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True)


def export_latest_branch(repo: Path, branch: str, source_subdir: str, destination: Path) -> None:
    run_git(repo, "fetch", "origin", branch)

    with tempfile.TemporaryDirectory() as temp_dir:
        archive_path = Path(temp_dir) / "source.tar"
        subprocess.run(
            [
                "git",
                "-C",
                str(repo),
                "archive",
                "--format=tar",
                "--output",
                str(archive_path),
                f"origin/{branch}",
                source_subdir,
            ],
            check=True,
        )

        extracted_root = Path(temp_dir) / "exported"
        extracted_root.mkdir(parents=True, exist_ok=True)
        with tarfile.open(archive_path) as archive:
            # Python 3.14 changes the default extraction filter; prefer a safe mode now.
            try:
                archive.extractall(extracted_root, filter="data")
            except TypeError:
                archive.extractall(extracted_root)

        exported_source = extracted_root / source_subdir
        shutil.copytree(exported_source, destination)


def export_text_file(repo: Path, branch: str, repo_path: str) -> str:
    candidates = [f"origin/{branch}:{repo_path}", f"HEAD:{repo_path}"]
    for candidate in candidates:
        completed = subprocess.run(
            ["git", "-C", str(repo), "show", candidate],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if completed.returncode == 0:
            return completed.stdout

    file_path = repo / repo_path
    if file_path.exists():
        return file_path.read_text(encoding="utf-8", errors="replace")

    raise subprocess.CalledProcessError(
        128,
        ["git", "-C", str(repo), "show", f"origin/{branch}:{repo_path}"],
    )


def reset_generated_targets() -> None:
    legacy_reference_root = DOCS_ROOT / "reference"
    if legacy_reference_root.exists():
        shutil.rmtree(legacy_reference_root)

    for legacy_dir in ("collection", "analysis"):
        legacy_path = DOCS_ROOT / legacy_dir
        if legacy_path.exists():
            shutil.rmtree(legacy_path)

    for tool in TOOLS:
        tool_root = DOCS_ROOT / tool["slug"]
        if tool_root.exists():
            shutil.rmtree(tool_root)


def clean_heading(value: str) -> str:
    value = re.sub(r"<a\s+name=.*?</a>", "", value, flags=re.IGNORECASE)
    value = re.sub(r"<[^>]+>", "", value)
    return value.strip()


def should_exclude(path: Path) -> bool:
    return path.name.lower() in EXCLUDED_NAMES


def is_hidden_mspti_api_context_dir(path: Path) -> bool:
    return False


def should_hide_from_nav(path: Path) -> bool:
    return path.name.lower() in NON_NAV_NAMES or is_hidden_mspti_api_context_dir(path)


def should_keep_display_path(path: Path) -> bool:
    relative_parts = [part.lower() for part in path.parts]
    if not relative_parts:
        return True

    # 检查目录部分是否匹配任何 DISPLAY_DIR_WHITELIST 模式
    for part in relative_parts[:-1] if path.is_file() else relative_parts:
        if any(fnmatch.fnmatch(part, pattern.lower()) for pattern in DISPLAY_DIR_WHITELIST):
            return True

    # 检查文件名是否匹配任何 DISPLAY_FILE_WHITELIST 模式（仅当是文件时）
    if path.is_file():
        filename = relative_parts[-1]
        if any(fnmatch.fnmatch(filename, pattern.lower()) for pattern in DISPLAY_FILE_WHITELIST):
            return True

    return False


def filter_display_tree(root: Path) -> None:
    for path in sorted(root.iterdir(), key=lambda item: len(item.parts), reverse=True):
        if path.name in {".nav.yml", "index.md", "README.md"}:
            continue
        if should_exclude(path):
            continue
        if should_keep_display_path(path.relative_to(root)):
            continue
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()


def repo_web_base(repo: Path) -> str:
    completed = subprocess.run(
        ["git", "-C", str(ROOT), "config", "--file", ".gitmodules", f"submodule.{repo.name}.url"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    url = completed.stdout.strip()
    if url.endswith(".git"):
        url = url[:-4]
    return url


def repo_blob_url(tool: dict, repo_path: str) -> str:
    return f"{tool['repo_web_base']}/blob/{tool['branch']}/{repo_path}"


def repo_tree_url(tool: dict, repo_path: str) -> str:
    return f"{tool['repo_web_base']}/tree/{tool['branch']}/{repo_path}"


def normalize_repo_path(path: Path) -> Path:
    normalized = Path(".")
    for part in path.parts:
        if part in {"", "."}:
            continue
        if part == "..":
            normalized = normalized.parent
            continue
        normalized /= part
    return normalized


def rewrite_missing_local_links(path: Path, root: Path, tool: dict, current_repo_path: Path | None = None) -> None:
    original_content = path.read_text(encoding="utf-8")
    content = original_content
    content = content.replace("](.//README.md", "](index.md")
    content = content.replace("](./README.md", "](index.md")
    content = content.replace("](../advanced_features/README.md", "](../advanced_features/index.md")
    content = content.replace("](./source/advanced_features/README.md", "](./source/advanced_features/index.md")
    content = content.replace("](./source/c_api/README.md", "](./source/c_api/index.md")
    content = content.replace("](./source/python_api/README.md", "](./source/python_api/index.md")
    content = content.replace("../../msprof-analyze/", "../../msprof-analyze/index.md")
    if current_repo_path is None:
        current_repo_path = Path(tool["source_subdir"]) / path.relative_to(root)

    def replace_markdown_link(match: re.Match[str]) -> str:
        label = match.group(1)
        target = match.group(2).strip()
        suffix = match.group(3) or ""
        if "://" in target or target.startswith(("#", "mailto:", "javascript:")):
            return match.group(0)

        clean_target = target.split("#", 1)[0].split("?", 1)[0]
        if not clean_target:
            return match.group(0)

        root_resolved = root.resolve()
        candidate = (path.parent / clean_target).resolve()
        try:
            candidate_relative = candidate.relative_to(root_resolved)
            if candidate.name.lower() == "readme.md":
                index_candidate = candidate.with_name("index.md")
                if index_candidate.exists():
                    rewritten_target = Path(index_candidate.relative_to(path.parent.resolve())).as_posix()
                    return f"[{label}]({rewritten_target}{suffix})"

            if candidate.exists():
                return match.group(0)

            repo_relative = Path(tool["source_subdir"]) / candidate_relative
            if (tool["repo"] / repo_relative).exists():
                remote = repo_tree_url(tool, repo_relative.as_posix()) if target.endswith("/") else repo_blob_url(tool, repo_relative.as_posix())
                return f"[{label}]({remote}{suffix})"
            return match.group(0)
        except ValueError:
            repo_candidate = normalize_repo_path(current_repo_path.parent / clean_target)
            if (tool["repo"] / repo_candidate).exists():
                remote = repo_tree_url(tool, repo_candidate.as_posix()) if target.endswith("/") else repo_blob_url(tool, repo_candidate.as_posix())
                return f"[{label}]({remote}{suffix})"
            if repo_candidate.name.lower() == "readme.md" and (tool["repo"] / "README.md").exists():
                return f"[{label}]({repo_blob_url(tool, 'README.md')}{suffix})"
            return match.group(0)

    rewritten = re.sub(r"\[([^\]]+)\]\(([^)]+?)(#[^)]+)?\)", replace_markdown_link, content)
    if rewritten != original_content:
        path.write_text(rewritten, encoding="utf-8")


def prune_tree(root: Path) -> None:
    for path in sorted(root.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        if should_exclude(path):
            if path.is_dir():
                shutil.rmtree(path)
            elif path.exists():
                path.unlink()


def sort_nav_items(paths: list[Path]) -> list[Path]:
    def sort_key(path: Path) -> tuple[int, str]:
        name = path.name
        lowered = name.lower()
        for index, pattern in enumerate(NAV_ORDER):
            if fnmatch.fnmatch(lowered, pattern.lower()):
                return (index, lowered)
        return (len(NAV_ORDER), lowered)
    return sorted(paths, key=sort_key)


def first_heading(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                return clean_heading(stripped.lstrip("#").strip())
    except UnicodeDecodeError:
        pass
    return path.stem.replace("_", " ")


def duplicate_readme_as_index(directory: Path) -> None:
    readme = directory / "README.md"
    index = directory / "index.md"
    if readme.exists() and not index.exists():
        shutil.copy2(readme, index)


def write_directory_nav(directory: Path) -> None:
    subdirectories = sort_nav_items(
        [
            child
            for child in directory.iterdir()
            if child.is_dir()
            and any(child.iterdir())
            and not should_exclude(child)
            and not should_hide_from_nav(child)
        ]
    )
    markdown_children = sort_nav_items(
        [
            child
            for child in directory.glob("*.md")
            if child.name.lower() != "readme.md" and not should_exclude(child)
        ]
    )

    nav_items: list[str] = []
    if (directory / "index.md").exists():
        nav_items.append("index.md")

    for child in subdirectories:
        nav_items.append(child.name)

    for child in markdown_children:
        if child.name.lower() == "index.md":
            continue
        nav_items.append(child.name)

    lines = ["collapse_single_pages: true"]
    if nav_items:
        lines.append("nav:")
        for item in nav_items:
            lines.append(f"  - {item}")
    lines.append("")
    (directory / ".nav.yml").write_text("\n".join(lines), encoding="utf-8")


def build_directory_indexes(root: Path, title_prefix: str) -> None:
    prune_tree(root)
    duplicate_readme_as_index(root)
    directories = sorted(
        [path for path in root.rglob("*") if path.is_dir()],
        key=lambda item: len(item.parts),
    )
    for directory in directories:
        duplicate_readme_as_index(directory)
        if (directory / "index.md").exists():
            continue

        markdown_children = sort_nav_items(
            child
            for child in directory.glob("*.md")
            if child.name.lower() != "index.md"
            and not (child.name == "README.md" and (directory / "index.md").exists())
            and not should_exclude(child)
        )
        subdirectories = sort_nav_items(
            child
            for child in directory.iterdir()
            if child.is_dir() and any(child.iterdir()) and not should_exclude(child)
        )
        if not markdown_children and not subdirectories:
            continue

        relative = directory.relative_to(root)
        heading = title_prefix if relative == Path(".") else relative.name.replace("-", " ").replace("_", " ")
        lines = [f"# {heading}", "", "", ""]

        if subdirectories:
            lines.extend(["## 子目录", ""])
            for child in subdirectories:
                target = child.relative_to(directory).as_posix() + "/"
                lines.append(f"- [{child.name}]({target})")
            lines.append("")

        if markdown_children:
            lines.extend(["## 页面", ""])
            for child in markdown_children:
                target = child.relative_to(directory).as_posix()
                lines.append(f"- [{first_heading(child)}]({target})")
            lines.append("")

        (directory / "index.md").write_text("\n".join(lines), encoding="utf-8")

    write_directory_nav(root)
    for directory in sorted([path for path in root.rglob("*") if path.is_dir()]):
        if any(directory.iterdir()):
            write_directory_nav(directory)


def write_tool_nav(path: Path, tool: dict) -> None:
    lines = [f"title: {tool['title']}", "nav:", "  - index.md"]
    featured_entries = [
        relative
        for _, relative in tool["entry_points"]
        if relative.startswith("source/") and (path.parent / relative).exists()
    ]
    if featured_entries:
        lines.append("  - 推荐阅读:")
        for relative in featured_entries:
            lines.append(f"    - {relative}")
    if tool.get("source_subdir") and (path.parent / "source").exists():
        lines.append("  - 文档目录: source")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def rewrite_repo_readme_links(content: str | None, tool: dict, source_root: Path) -> str:
    if content is None:
        content = ""
    replacements = {
        "./docs/zh/": "./source/",
        "docs/zh/": "source/",
        "./docs/": "./source/",
        "./docs/zh": "./source",
        "docs/zh": "source",
        "./docs": "./source",
    }
    for old, new in replacements.items():
        content = content.replace(old, new)

    # Allow Markdown links inside aligned HTML wrappers from repo READMEs.
    content = content.replace('<div align="center">', '<div align="center" markdown="1">')
    content = content.replace("<div align='center'>", '<div align="center" markdown="1">')

    filtered_lines = []
    for line in content.splitlines():
        lowered = line.lower()
        if "/source/legal/" in lowered:
            continue
        if "contributing.md" in lowered or "contributed" in lowered:
            continue
        filtered_lines.append(line)

    rewritten = "\n".join(filtered_lines) + "\n"
    rewritten = rewritten.replace("./source/LICENSE", repo_blob_url(tool, "docs/LICENSE"))
    temp_readme = source_root.parent / "_repo_readme_rewrite.md"
    temp_readme.write_text(rewritten, encoding="utf-8")
    rewrite_missing_local_links(temp_readme, source_root, tool, current_repo_path=Path(tool["repo_readme"]))
    final_text = temp_readme.read_text(encoding="utf-8")
    temp_readme.unlink(missing_ok=True)
    return final_text


def generate_tool_page(tool: dict) -> None:
    tool = {**tool, "repo_web_base": repo_web_base(tool["repo"])}
    tool_root = DOCS_ROOT / tool["slug"]
    source_root = tool_root / "source"
    tool_root.mkdir(parents=True, exist_ok=True)
    source_subdir = tool.get("source_subdir")

    if source_subdir:
        export_latest_branch(tool["repo"], tool["branch"], source_subdir, source_root)
        filter_display_tree(source_root)
        build_directory_indexes(source_root, tool["title"])
        if tool["slug"] == "mspti":
            for api_dir in ("c_api", "python_api"):
                api_root = source_root / api_dir
                if api_root.exists():
                    write_directory_nav(api_root)
                    context_dir = api_root / "context"
                    if context_dir.exists():
                        write_directory_nav(context_dir)
        for markdown_path in source_root.rglob("*.md"):
            rewrite_missing_local_links(markdown_path, source_root, tool)
    write_tool_nav(tool_root / ".nav.yml", tool)
    readme_text = export_text_file(tool["repo"], tool["branch"], tool["repo_readme"])
    if source_subdir:
        readme_text = rewrite_repo_readme_links(readme_text, tool, source_root)
    repo_notice = "\n".join(
        [
            "!!! info",
            f"    更多信息，欢迎查看源码仓: [{tool['title']}]({tool['repo_web_base']})",
            "",
        ]
    )
    (tool_root / "index.md").write_text(f"{repo_notice}{readme_text}", encoding="utf-8")


def main() -> None:
    reset_generated_targets()
    for tool in TOOLS:
        generate_tool_page(tool)


if __name__ == "__main__":
    main()

# TODO：
# 更新小助手图片并替换链接