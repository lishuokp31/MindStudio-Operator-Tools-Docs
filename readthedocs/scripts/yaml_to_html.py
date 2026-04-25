import yaml
import os
import re
from collections import defaultdict

# ===================== 自动获取当前脚本所在目录 =====================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ===================== 固定后缀列表 =====================
ALLOWED_SUFFIXES = {"A2", "A3", "A5", "310B"}

# ===================== 版本合并函数 =====================
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
        unique_suffixes = sorted(list(set(suffixes)))
        combined = "/".join(unique_suffixes)
        full_name = f"{prefix} {combined}"

        any_part = any(part_states.get(f"{prefix} {s}", False) for s in suffixes)
        if any_part:
            merged.append(f"{full_name}:part")
        else:
            merged.append(full_name)

    merged.extend(original_items)
    return merged

# ===================== 核心函数=====================
def generate_feature_tree(
    yaml_path: str = "feature_tree.yaml",
    template_path: str = "feature_template.html",
    output_path: str = "feature_tree_final.html",
    
    # 模板里的注入点（单个标签）
    inject_marker: str = "<!-- FEATURE_TREE_INJECT_HERE -->",
    
    # 最终目标文件里的替换区域（双标签）
    start_marker: str = "<!-- FEATURE_TREE_START -->",
    end_marker: str = "<!-- FEATURE_TREE_END -->"
) -> bool:
    try:
        # 路径自动基于脚本目录
        yaml_abs = os.path.join(SCRIPT_DIR, yaml_path)
        template_abs = os.path.join(SCRIPT_DIR, template_path)
        output_abs = os.path.join(SCRIPT_DIR, output_path)

        # ==============================================
        # 步骤 1：读取 YAML → 生成树 HTML
        # ==============================================
        with open(yaml_abs, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

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

        # ==============================================
        # 步骤 2：读取模板 → 把树插入模板的单个标签位置
        # ==============================================
        with open(template_abs, "r", encoding="utf-8") as f:
            template_content = f.read()

        # 把生成的树插入模板
        full_html = template_content.replace(inject_marker, tree_html)

        # ==============================================
        # 步骤 3：读取目标文件 → 替换双标签之间的内容
        # ==============================================
        with open(output_abs, "r", encoding="utf-8") as f:
            target_content = f.read()

        # 正则匹配：只替换两个标记之间
        pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)
        final_content = pattern.sub(
            f"{start_marker}\n{full_html}\n{end_marker}",
            target_content
        )

        # ==============================================
        # 步骤 4：写入最终文件
        # ==============================================
        with open(output_abs, "w", encoding="utf-8") as f:
            f.write(final_content)

        print("生成成功！完整流程执行完毕")
        print(f"从 {yaml_path} 读取数据")
        print(f"插入模板 {template_path}")
        print(f"写入目标文件 {output_path} 标记区域")
        return True

    except Exception as e:
        print(f"生成失败：{str(e)}")
        return False

# ===================== 命令行运行 =====================
if __name__ == "__main__":
    generate_feature_tree()