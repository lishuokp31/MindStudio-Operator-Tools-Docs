import yaml
import os
import re
from collections import defaultdict

# ===================== 路径 =====================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ===================== 版本标签合并 =====================
ALLOWED_SUFFIXES = {"A2", "A3", "A5", "310B"}


def merge_version_labels(version_list):
    groups = defaultdict(list)
    part_states = {}
    original_items = []

    for v in version_list:
        is_part = ":part" in v
        v_clean = v.split(":")[0].strip()
        words = v_clean.split()
        if not words:
            continue
        suffix = words[-1]
        if suffix in ALLOWED_SUFFIXES:
            prefix = " ".join(words[:-1])
            groups[prefix].append(suffix)
            part_states[f"{prefix} {suffix}"] = is_part
        else:
            original_items.append(v)

    merged = []
    for prefix, suffixes in groups.items():
        unique = sorted(set(suffixes))
        full = f"{prefix} {'/'.join(unique)}"
        any_part = any(part_states.get(f"{prefix} {s}", False) for s in suffixes)
        merged.append(f"{full}:part" if any_part else full)
    merged.extend(original_items)
    return merged


# ===================== 公共 HTML 生成函数 =====================

def _render_versions(version_list: list[str]) -> str:
    """将版本列表渲染为 HTML 标签。"""
    if not version_list:
        return ""
    html = ""
    for v in merge_version_labels(version_list):
        is_part = ":part" in v
        name = v.split(":")[0] if is_part else v
        cls = "v-part" if is_part else "v-support"
        html += f'<span class="version-label {cls}">{name}</span>'
    return html


def _build_node(item: dict, level: int = 1, path: str = "0") -> str:
    """递归构建单个树节点的 HTML（可被所有生成器复用）。"""
    name = item["name"]
    icon = item.get("icon", "")
    children = item.get("children", [])
    has_child = bool(children)

    icon_html = f'<i class="fa-solid fa-{icon} icon"></i>' if icon else ""
    ver_html = _render_versions(item.get("version", [])) if level == 4 else ""

    example_html = ""
    if "example_link" in item:
        example_html = f'<a class="ft-example-btn" href="{item["example_link"]}" title="查看样例">📦 跳转到样例</a>'

    toggle_cls = "expanded" if (level == 1 and has_child) else "collapsed"
    toggle_no = "no-toggle" if not has_child else ""
    disp = "display: none;" if not (level == 1 and has_child) else ""

    html = (
        f'<li class="tree-node" data-ft-path="{path}">'
        f'<div class="tree-item">'
        f'<span class="toggle-btn {toggle_cls} {toggle_no}"></span>'
        f'<span class="feature-name">{icon_html}{name}</span>'
        f'<div class="feature-versions">{ver_html}</div>'
        f'{example_html}'
        f'</div>'
    )
    if has_child:
        html += f'<ul class="tree-child" style="{disp}">'
        for i, child in enumerate(children):
            html += _build_node(child, level + 1, f"{path}-{i}")
        html += "</ul>"
    html += "</li>"
    return html


def _build_tree(features: list[dict]) -> str:
    """将特性列表渲染为完整的 <ul> 树 HTML。"""
    return "".join(_build_node(f, path=str(i)) for i, f in enumerate(features))


def _inject_to_output(
    full_html: str,
    output_abs: str,
    start_marker: str,
    end_marker: str,
) -> None:
    """将完整 HTML 写入目标文件中的标记区域。"""
    with open(output_abs, "r", encoding="utf-8") as f:
        target = f.read()
    pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)
    result = pattern.sub(f"{start_marker}\n{full_html}\n{end_marker}", target)
    with open(output_abs, "w", encoding="utf-8") as f:
        f.write(result)


# ===================== 单树生成 =====================

def generate_feature_tree(
    yaml_path: str = "feature_tree.yaml",
    template_path: str = "feature_template.html",
    output_path: str = "feature_tree_final.html",
    inject_marker: str = "<!-- FEATURE_TREE_INJECT_HERE -->",
    start_marker: str = "<!-- FEATURE_TREE_START -->",
    end_marker: str = "<!-- FEATURE_TREE_END -->",
) -> bool:
    """从单个 YAML 生成特性树，注入目标文件。"""
    try:
        ya = os.path.join(SCRIPT_DIR, yaml_path)
        ta = os.path.join(SCRIPT_DIR, template_path)
        oa = os.path.join(SCRIPT_DIR, output_path)

        with open(ya, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        with open(ta, encoding="utf-8") as f:
            template = f.read()

        tree_html = _build_tree(data["features"])
        full_html = template.replace(inject_marker, tree_html)
        _inject_to_output(full_html, oa, start_marker, end_marker)

        print(f"特性树生成成功 → {output_path}")
        return True
    except Exception as e:
        print(f"生成失败：{e}")
        return False


# ===================== SIMD + SIMT 合并为一棵树 =====================

_SIMT_L1_MAP = {
    "设计": "算子设计",
    "开发": "算子开发",
    "测试": "算子测试",
    "调试": "算子调试",
    "调优": "算子调优",
}


def _merge_trees(base: list[dict], other: list[dict]) -> list[dict]:
    """递归合并两棵树：同名节点合并，版本取并集。"""
    result: list[dict] = []
    matched = [False] * len(other)

    for node_a in base:
        merged = dict(node_a)
        idx = next((i for i, nb in enumerate(other)
                    if not matched[i] and nb["name"] == node_a["name"]), None)
        if idx is not None:
            nb = other[idx]
            matched[idx] = True
            ca = merged.get("children", [])
            cb = nb.get("children", [])
            if ca and cb:
                merged["children"] = _merge_trees(ca, cb)
            elif cb:
                merged["children"] = list(cb)
            elif ca:
                merged["children"] = list(ca)
            va, vb = merged.get("version", []), nb.get("version", [])
            if vb:
                seen = set(va)
                for v in vb:
                    if v not in seen:
                        va.append(v)
                        seen.add(v)
                if va:
                    merged["version"] = va
        elif "children" in merged:
            merged["children"] = list(merged["children"])
        result.append(merged)

    for i, nb in enumerate(other):
        if not matched[i]:
            result.append(dict(nb))
    return result


def generate_merged_feature_tree(
    simd_yaml: str = "feature_tree_SIMD.yaml",
    simt_yaml: str = "feature_tree_SIMT.yaml",
    template_path: str = "feature_template.html",
    output_path: str = "../docs/overview/index.md",
    inject_marker: str = "<!-- FEATURE_TREE_INJECT_HERE -->",
    start_marker: str = "<!-- FEATURE_TREE_START -->",
    end_marker: str = "<!-- FEATURE_TREE_END -->",
) -> bool:
    """将 SIMD 和 SIMT YAML 合并为一棵树，注入 overview 页面。"""
    try:
        sa = os.path.join(SCRIPT_DIR, simd_yaml)
        ta = os.path.join(SCRIPT_DIR, simt_yaml)
        pa = os.path.join(SCRIPT_DIR, template_path)
        oa = os.path.join(SCRIPT_DIR, output_path)

        with open(sa, encoding="utf-8") as f:
            simd = yaml.safe_load(f)
        with open(ta, encoding="utf-8") as f:
            simt = yaml.safe_load(f)
        with open(pa, encoding="utf-8") as f:
            template = f.read()

        # 映射 SIMT 一级名称
        simt_features = []
        for n in simt["features"]:
            m = dict(n)
            m["name"] = _SIMT_L1_MAP.get(n["name"], n["name"])
            simt_features.append(m)

        merged = _merge_trees(simd["features"], simt_features)

        tree_html = _build_tree(merged)
        full_html = template.replace(inject_marker, tree_html)
        _inject_to_output(full_html, oa, start_marker, end_marker)

        def _cnt(n):
            return 1 + sum(_cnt(c) for c in n.get("children", []))
        total = sum(_cnt(f) for f in merged)
        all_ver = len(simd.get("all_versions", [])) + len(simt.get("all_versions", []))
        print(f"合并特性树生成成功！{len(merged)} 一级，{total} 节点，~{all_ver} 版本 → {output_path}")
        return True
    except Exception as e:
        print(f"合并树生成失败：{e}")
        return False


# ===================== CLI =====================
if __name__ == "__main__":
    generate_feature_tree()
