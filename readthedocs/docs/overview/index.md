---
hide:
  - navigation
  - toc
---


# 算子工具全景

## 算子工具链

<!-- <style>
.ai-arch-container {
    --ai-accent-blue: #3b82f6;
    --ai-text-dark: #1e293b;
    --ai-bg-section: #f8fafc;
    --ai-transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px 20px 40px 20px;
    box-sizing: border-box;
}

.ai-arch-container * {
    box-sizing: border-box;
}

.ai-arch-container .arch-wrapper {
    position: relative;
    display: flex;
    flex-direction: row;
    gap: 24px;
    padding: 40px;
    background: #ffffff;
    border-radius: 24px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08), 0 1px 3px rgba(0, 0, 0, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.8);
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
}

.ai-arch-container .main-layers {
    display: flex;
    flex-direction: column;
    gap: 20px;
    flex: 1;
}

.ai-arch-container .layer-section {
    display: flex;
    background: var(--ai-bg-section);
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid rgba(226, 232, 240, 0.7);
    transition: var(--ai-transition);
}

.ai-arch-container .layer-title {
    width: 48px;
    writing-mode: vertical-lr;
    text-orientation: mixed;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #e2e8f0;
    color: #475569;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 2px;
    border-right: 1px solid rgba(203, 213, 225, 0.5);
}

.ai-arch-container .layer-content {
    flex: 1;
    padding: 20px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
}

.ai-arch-container .layer-content-3 {
    grid-template-columns: repeat(3, 1fr);
}

.ai-arch-container .module {
    position: relative;
    background: #ffffff;
    padding: 14px 20px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    font-weight: 700;
    cursor: pointer;
    transition: var(--ai-transition);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.04);
    color: var(--ai-text-dark);
    border: 1px solid rgba(226, 232, 240, 0.8);
    text-align: center;
}

.ai-arch-container .module:hover {
    background: var(--ai-accent-blue);
    color: #ffffff !important;
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(59, 130, 246, 0.25);
    border-color: var(--ai-accent-blue);
}

.ai-arch-container .tool-card {
    width: 100px;
    background: var(--ai-bg-section);
    border: 1px solid rgba(226, 232, 240, 0.8);
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px 10px;
    text-align: center;
    font-size: 14px;
    font-weight: 700;
    transition: var(--ai-transition);
    cursor: pointer;
    color: var(--ai-text-dark);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
}

.ai-arch-container .tool-card:hover {
    background: #1e293b;
    color: #ffffff;
    transform: scale(1.05);
}

.ai-arch-container #dynamic-preview {
    position: absolute;
    width: 260px;
    background: #ffffff;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
    pointer-events: none;
    opacity: 0;
    transform: translateX(10px);
    transition: opacity 0.3s, transform 0.3s;
    z-index: 2000;
    border: 1px solid rgba(0, 0, 0, 0.06);
}

.ai-arch-container #dynamic-preview.active {
    opacity: 1;
    transform: translateX(0);
}

.ai-arch-container .preview-h {
    font-weight: 800;
    color: var(--ai-accent-blue);
    margin-bottom: 8px;
    font-size: 15px;
}

.ai-arch-container .preview-p {
    font-size: 13px;
    color: #64748b;
    line-height: 1.6;
    margin: 0;
}

.ai-arch-container .span-2 { grid-column: span 2; }
.ai-arch-container .flex-center { justify-content: center; }
.ai-arch-container .justify-content-around { justify-content: space-around; }

@media (max-width: 850px) {
    .ai-arch-container .arch-wrapper {
        flex-direction: column;
        align-items: stretch;
    }

    .ai-arch-container .tool-card {
        width: 100%;
        flex-direction: row;
        padding: 15px;
        gap: 15px;
    }

    .ai-arch-container #dynamic-preview {
        display: none !important;
    }
}

@media (max-width: 550px) {
    .ai-arch-container {
        padding: 20px 10px;
    }

    .ai-arch-container .layer-content,
    .ai-arch-container .layer-content-3 {
        grid-template-columns: 1fr;
        padding: 12px;
    }

    .ai-arch-container .span-2 {
        grid-column: span 1;
    }

    .ai-arch-container .layer-title {
        width: 36px;
        font-size: 11px;
    }

    .ai-arch-container .module {
        font-size: 13px;
        padding: 12px;
    }
}
</style> -->

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>开源AI工具 - 全功能特性树</title>
    <!-- 引入图标库 -->
    <link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Segoe UI", "Microsoft YaHei", sans-serif;
            transition: color 0.3s ease, background-color 0.3s ease, border-color 0.3s ease;
        }

        :root {
            --bg: #f0f2f5;
            --card: #ffffff;
            --title: #111827;
            --text1: #1f2937;
            --text2: #374151;
            --text3: #4b5563;
            --border: #e5e7eb;
            --line: #d1d5db;
            --hover: #f9fafb;
            --color-ai: #2563eb;
            --color-code: #059669;
            --color-plugin: #7c3aed;
            --color-tool: #d946ef;
            --color-deploy: #ea580c;
        }

        [data-theme="dark"] {
            --bg: #121212;
            --card: #1e1e1e;
            --title: #f9fafb;
            --text1: #f3f4f6;
            --text2: #e5e7eb;
            --text3: #d1d5db;
            --border: #333333;
            --line: #444444;
            --hover: #2d2d2d;
        }

        body {
            padding: 30px;
            background-color: var(--bg);
        }

        .feature-tree-container {
            max-width: 1300px;
            margin: 0 auto;
            background: var(--card);
            border-radius: 18px;
            padding: 32px;
            box-shadow: 0 8px 28px rgba(0, 0, 0, 0.08);
            border: 1px solid var(--border);
        }

        .tool-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
            flex-wrap: wrap;
            gap: 12px;
        }

        .tree-title {
            font-size: 26px;
            font-weight: bold;
            color: var(--title);
            margin: 0;
        }

        .action-group {
            display: flex;
            gap: 10px;
        }

        .btn {
            padding: 8px 14px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 6px;
            background: var(--hover);
            color: var(--text2);
        }

        .btn:hover {
            opacity: 0.9;
            transform: translateY(-1px);
        }

        .btn-primary {
            background: #2563eb;
            color: white;
        }

        /* 版本标签 */
        .version-label {
            display: inline-block;
            margin-left: 10px;
            font-size: 12px;
            padding: 3px 9px;
            border-radius: 12px;
            font-weight: bold;
            letter-spacing: 0.4px;
            white-space: nowrap;
        }

        .v-support {
            background-color: #ecfdf5;
            color: #067f4d;
            border: 1px solid #a7f3d0;
        }

        .v-unsupport {
            background-color: #fef2f2;
            color: #dc2626;
            border: 1px solid #fecaca;
        }

        .v-part {
            background-color: #fffbeb;
            color: #d97706;
            border: 1px solid #fcd34d;
        }

        [data-theme="dark"] .v-support {
            background-color: #064e3b;
            color: #a7f3d0;
            border-color: #047857;
        }

        [data-theme="dark"] .v-unsupport {
            background-color: #7f1d1d;
            color: #fecaca;
            border-color: #b91c1c;
        }

        [data-theme="dark"] .v-part {
            background-color: #78350f;
            color: #fcd34d;
            border-color: #d97706;
        }

        /* 树形结构 */
        .tree-node {
            list-style: none;
            padding-left: 32px;
            position: relative;
        }

        .tree-root {
            padding-left: 0;
        }

        .tree-item {
            display: flex;
            align-items: center;
            padding: 10px 0;
            cursor: pointer;
            transition: all 0.25s ease;
            color: var(--text2);
        }

        .tree-item:hover {
            background-color: var(--hover);
            border-radius: 8px;
            padding-left: 6px;
        }

        /* 展开箭头 */
        .toggle-btn {
            width: 18px;
            height: 18px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            margin-right: 10px;
            font-size: 12px;
            color: var(--text3);
            user-select: none;
            flex-shrink: 0;
        }

        .toggle-btn.collapsed::after {
            content: "▶";
        }

        .toggle-btn.expanded::after {
            content: "▼";
        }

        .no-toggle {
            visibility: hidden;
        }

        /* 连接线 */
        .tree-node::before {
            content: "";
            position: absolute;
            top: 0;
            left: 14px;
            width: 1px;
            height: 100%;
            background-color: var(--line);
        }

        .tree-item::before {
            content: "";
            position: absolute;
            top: 21px;
            left: 14px;
            width: 18px;
            height: 1px;
            background-color: var(--line);
        }

        .tree-root>.tree-node::before {
            display: none;
        }

        .tree-root>.tree-node>.tree-item::before {
            display: none;
        }

        /* 功能名称 + 图标 */
        .feature-name {
            flex: 1;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .feature-versions {
            display: flex;
            gap: 6px;
            flex-shrink: 0;
        }

        .icon {
            width: 16px;
            text-align: center;
            flex-shrink: 0;
        }

        /* 层级样式 */
        /* 一级节点 */
        .tree-root>.tree-node>.tree-item .feature-name {
            font-size: 18px;
            font-weight: bold;
            color: var(--text1);
        }

        /* 二级节点：按模块自动配色 */
        .tree-root>.tree-node>.tree-child>.tree-node>.tree-item .feature-name {
            font-size: 16px;
            font-weight: 500;
            color: var(--color-ai);
        }

        .tree-root>.tree-node:nth-child(2)>.tree-child>.tree-node>.tree-item .feature-name {
            color: var(--color-code);
        }

        .tree-root>.tree-node:nth-child(3)>.tree-child>.tree-node>.tree-item .feature-name {
            color: var(--color-plugin);
        }

        .tree-root>.tree-node:nth-child(4)>.tree-child>.tree-node>.tree-item .feature-name {
            color: var(--color-tool);
        }

        .tree-root>.tree-node:nth-child(5)>.tree-child>.tree-node>.tree-item .feature-name {
            color: var(--color-deploy);
        }

        /* 三级及以下 */
        .tree-child .tree-child .tree-item .feature-name {
            font-size: 14px;
            color: var(--text3);
        }
    </style>
</head>
<body>
    <div class="feature-tree-container">
        <div class="tool-bar">
            <h2 class="tree-title">开源AI工具 - 全功能特性树</h2>
            <div class="action-group">
                <button class="btn" id="expandAll"><i class="fa-solid fa-plus"></i> 全部展开</button>
                <button class="btn" id="collapseAll"><i class="fa-solid fa-minus"></i> 全部收起</button>
                <button class="btn btn-primary" id="toggleDark"><i class="fa-solid fa-moon"></i> 暗黑模式</button>
            </div>
        </div>

        <ul class="tree-root" id="featureTree">
            <!-- 一级模块 -->
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn expanded"></span>
                    <span class="feature-name">
                        <i class="fa-solid fa-brain icon" style="color:#2563eb"></i>
                        AI 核心能力模块
                    </span>
                    <div class="feature-versions">
                        <span class="version-label v-support">V1.0</span>
                        <span class="version-label v-support">V2.0</span>
                        <span class="version-label v-support">V3.0</span>
                    </div>
                </div>
                <ul class="tree-child">
                    <li class="tree-node">
                        <div class="tree-item">
                            <span class="toggle-btn collapsed"></span>
                            <span class="feature-name">
                                <i class="fa-solid fa-file-lines icon"></i>
                                文本生成能力
                            </span>
                            <div class="feature-versions">
                                <span class="version-label v-support">V1.0</span>
                                <span class="version-label v-support">V2.0</span>
                                <span class="version-label v-support">V3.0</span>
                            </div>
                        </div>
                        <ul class="tree-child" style="display: none;">
                            <li class="tree-node">
                                <div class="tree-item">
                                    <span class="toggle-btn no-toggle"></span>
                                    <span class="feature-name">通用文案生成</span>
                                    <div class="feature-versions">
                                        <span class="version-label v-support">V1.0</span>
                                        <span class="version-label v-support">V2.0</span>
                                        <span class="version-label v-support">V3.0</span>
                                    </div>
                                </div>
                            </li>
                            <li class="tree-node">
                                <div class="tree-item">
                                    <span class="toggle-btn no-toggle"></span>
                                    <span class="feature-name">专业领域生成</span>
                                    <div class="feature-versions">
                                        <span class="version-label v-unsupport">V1.0</span>
                                        <span class="version-label v-part">V2.0</span>
                                        <span class="version-label v-support">V3.0</span>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </li>

                    <li class="tree-node">
                        <div class="tree-item">
                            <span class="toggle-btn collapsed"></span>
                            <span class="feature-name">
                                <i class="fa-solid fa-images icon"></i>
                                多模态处理
                            </span>
                            <div class="feature-versions">
                                <span class="version-label v-unsupport">V1.0</span>
                                <span class="version-label v-support">V2.0</span>
                                <span class="version-label v-support">V3.0</span>
                            </div>
                        </div>
                        <ul class="tree-child" style="display: none;">
                            <li class="tree-node">
                                <div class="tree-item">
                                    <span class="toggle-btn no-toggle"></span>
                                    <span class="feature-name">图片理解</span>
                                    <div class="feature-versions">
                                        <span class="version-label v-unsupport">V1.0</span>
                                        <span class="version-label v-support">V2.0</span>
                                        <span class="version-label v-support">V3.0</span>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </li>
                </ul>
            </li>

            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed"></span>
                    <span class="feature-name">
                        <i class="fa-solid fa-code icon" style="color:#059669"></i>
                        开发与API能力
                    </span>
                    <div class="feature-versions">
                        <span class="version-label v-part">V1.0</span>
                        <span class="version-label v-support">V2.0</span>
                        <span class="version-label v-support">V3.0</span>
                    </div>
                </div>
                <ul class="tree-child" style="display: none;"></ul>
            </li>

            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed"></span>
                    <span class="feature-name">
                        <i class="fa-solid fa-puzzle-piece icon" style="color:#7c3aed"></i>
                        插件与扩展生态
                    </span>
                    <div class="feature-versions">
                        <span class="version-label v-unsupport">V1.0</span>
                        <span class="version-label v-part">V2.0</span>
                        <span class="version-label v-support">V3.0</span>
                    </div>
                </div>
                <ul class="tree-child" style="display: none;"></ul>
            </li>
        </ul>
    </div>

    <script>
        // 展开/收起单个节点
        document.querySelectorAll('.toggle-btn').forEach(btn => {
            btn.addEventListener('click', function (e) {
                e.stopPropagation();
                const parentItem = this.closest('.tree-item');
                const childList = parentItem.nextElementSibling;
                if (!childList) return;

                const isHidden = childList.style.display === 'none';
                childList.style.display = isHidden ? 'block' : 'none';
                this.classList.toggle('collapsed', !isHidden);
                this.classList.toggle('expanded', isHidden);
            });
        });

        // 全部展开
        document.getElementById('expandAll').addEventListener('click', () => {
            document.querySelectorAll('.tree-child').forEach(el => {
                el.style.display = 'block';
            });
            document.querySelectorAll('.toggle-btn').forEach(btn => {
                btn.classList.remove('collapsed');
                btn.classList.add('expanded');
            });
        });

        // 全部收起
        document.getElementById('collapseAll').addEventListener('click', () => {
            document.querySelectorAll('.tree-child').forEach(el => {
                el.style.display = 'none';
            });
            document.querySelectorAll('.toggle-btn').forEach(btn => {
                if (!btn.classList.contains('no-toggle')) {
                    btn.classList.remove('expanded');
                    btn.classList.add('collapsed');
                }
            });
        });

        // 暗黑模式切换
        const darkBtn = document.getElementById('toggleDark');
        const icon = darkBtn.querySelector('i');
        const text = darkBtn.childNodes[1];

        darkBtn.addEventListener('click', () => {
            const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
            if (isDark) {
                document.documentElement.removeAttribute('data-theme');
                icon.className = 'fa-solid fa-moon';
                text.textContent = ' 暗黑模式';
            } else {
                document.documentElement.setAttribute('data-theme', 'dark');
                icon.className = 'fa-solid fa-sun';
                text.textContent = ' 明亮模式';
            }
        });
    </script>
</body>
</html>



## TODO:工具总览和描述


## 相关入口

<style>
.grid.cards .md-typeset hr {
    width: 100%;
    margin: 0.5rem 0 1rem 0;
    border: none;
    height: 1px;
    background: linear-gradient(90deg,
        rgba(0,0,0,0.08) 0%,
        rgba(0,0,0,0.2) 40%,
        rgba(0,0,0,0.2) 60%,
        rgba(0,0,0,0.08) 100%);
}

.grid.cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}

.grid.cards .card {
    height: 100%;
    display: flex;
    flex-direction: column;
}

.grid.cards .card hr {
    width: 100%;
}

[data-md-color-scheme="slate"] .grid.cards .md-typeset hr {
    background: linear-gradient(90deg,
        rgba(255,255,255,0.08) 0%,
        rgba(255,255,255,0.2) 40%,
        rgba(255,255,255,0.2) 60%,
        rgba(255,255,255,0.08) 100%);
}
</style>

<div class="grid cards" markdown>

-   **[msOT](../msot/)**

    ---

    算子开发工具链，聚焦算子开发中的关键挑战。

-   **[msKPP](../mskpp/)**

    ---

    性能仿真工具，支持基于算子表达式快速预测其在给定算法实现下的性能上限。

-   **[msOpGen](../msopgen/)**

    ---

    算子工程自动生成工具，支持多种类型工程的快速构建。

-   **[msSanitizer](../mssanitizer/)**

    ---

    算子异常检测工具，提供内存越界、数据竞争、未初始化访问及同步异常四大检测能力。

-   **[msDebug](../msdebug/)**

    ---

    算子调试工具，用于调试在 NPU 侧运行的算子程序，为开发者提供关键调试能力。

-   **[msOpProf](../msopprof/)**

    ---

    算子调优工具，采集与分析运行在昇腾AI处理器上的算子关键性能指标，显著提升性能分析效率。

-   **[msOpTuner](../msoptuner/)**

    ---

    算子Tiling寻优工具，支持基于算子表达式快速预测其在给定算法实现下的性能上限。

-   **[msKL](../mskl/)**

    ---

    算子轻量化调用工具，支持在Python脚本中快速实现Kernel下发代码生成、编译及运行Kernel。

-   **[msOpCom](../msopcom/)**

    ---

    算子工具基础组件，提供算子工具运行所需的桩函数注入、接口劫持等功能。

-   **[msTX](../mstx/)**

    ---

    算子工具扩展接口库，自定义采集时间段或者关键函数的开始和结束时间点，识别关键函数或迭代等信息，对性能和算子问题快速定界。

</div>

