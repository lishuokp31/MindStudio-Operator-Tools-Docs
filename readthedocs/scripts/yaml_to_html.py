import yaml
import os
from collections import defaultdict

# ===================== 自动获取当前脚本所在目录 =====================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ===================== 固定后缀列表（只合并这些！） =====================
ALLOWED_SUFFIXES = {"A2", "A3", "A5", "310B"}

# ===================== 极简版本合并函数（无正则，硬匹配） =====================
def merge_version_labels(version_list):
    groups = defaultdict(list)  # key: 前缀, value: [后缀]
    part_states = {}  # 记录是否是部分支持
    original_items = []

    # 第一步：拆分 前缀 + 后缀
    for v in version_list:
        is_part = ":part" in v
        v_clean = v.split(":")[0].strip()
        words = v_clean.split()

        if not words:
            continue

        # 最后一段是不是我们允许的后缀？
        suffix = words[-1]
        if suffix in ALLOWED_SUFFIXES:
            prefix = " ".join(words[:-1])
            groups[prefix].append(suffix)
            part_states[f"{prefix} {suffix}"] = is_part
        else:
            original_items.append(v)

    # 第二步：合并同前缀的后缀
    merged = []
    for prefix, suffixes in groups.items():
        unique_suffixes = sorted(list(set(suffixes)))  # 去重 + 排序
        combined = " / ".join(unique_suffixes)
        full_name = f"{prefix} {combined}"

        # 只要有一个是 part，就标记为 part（你也可以改成只要一个支持就算支持）
        any_part = any(part_states.get(f"{prefix} {s}", False) for s in suffixes)
        if any_part:
            merged.append(f"{full_name}:part")
        else:
            merged.append(full_name)

    # 第三步：合并无法分组的原始项
    merged.extend(original_items)
    return merged

# ===================== 核心工具函数 =====================
def generate_feature_tree(
    yaml_path: str = "feature_tree.yaml",
    template_path: str = "feature_template.html",
    output_path: str = "feature_tree_final.html",
    inject_marker: str = "<!-- FEATURE_TREE_INJECT_HERE -->"
) -> bool:
    try:
        yaml_abs = os.path.join(SCRIPT_DIR, yaml_path)
        template_abs = os.path.join(SCRIPT_DIR, template_path)
        output_abs = os.path.join(SCRIPT_DIR, output_path)

        with open(yaml_abs, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        # 递归生成节点
        def build_node(item, level=1):
            name = item["name"]
            icon = item.get("icon", "")
            children = item.get("children", [])
            has_child = len(children) > 0

            icon_html = f'<i class="fa-solid fa-{icon} icon"></i>' if icon else ""
            ver_html = ""

            if level == 4 and "version" in item:
                merged = merge_version_labels(item["version"])
                for v in merged:
                    state = "support"
                    v_name = v
                    if ":part" in v:
                        v_name = v.split(":")[0]
                        state = "part"
                    cls = "v-part" if state == "part" else "v-support"
                    ver_html += f'<span class="version-label {cls}">{v_name}</span>'

            toggle_cls = "expanded" if (level == 1 and has_child) else "collapsed"
            toggle_no = "no-toggle" if not has_child else ""
            display = "display: none;" if not (level == 1 and has_child) else ""

            html = f"""
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn {toggle_cls} {toggle_no}"></span>
                    <span class="feature-name">{icon_html}{name}</span>
                    <div class="feature-versions">{ver_html}</div>
                </div>
            """
            if has_child:
                html += f'<ul class="tree-child" style="{display}">'
                for child in children:
                    html += build_node(child, level + 1)
                html += "</ul>"
            html += "</li>"
            return html

        tree_html = ""
        for feat in data["features"]:
            tree_html += build_node(feat)

        with open(template_abs, "r", encoding="utf-8") as f:
            template_content = f.read()

        final_content = template_content.replace(inject_marker, tree_html)

        with open(output_abs, "w", encoding="utf-8") as f:
            f.write(final_content)

        print("生成完成！")
        return True

    except Exception as e:
        print(f"生成失败：{str(e)}")
        return False

# ===================== 命令行运行 =====================
if __name__ == "__main__":
    generate_feature_tree()