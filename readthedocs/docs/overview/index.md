<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>开源AI工具 - 全功能特性树</title>
    <link rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin:0; padding:0; box-sizing:border-box;
            font-family: "Segoe UI", "Microsoft YaHei", sans-serif;
            transition: color 0.3s, background 0.3s, border-color 0.3s;
        }
        :root {
            --bg:#f0f2f5; --card:#fff; --title:#111827; --text1:#1f2937; --text2:#374151; --text3:#4b5563;
            --border:#e5e7eb; --line:#d1d5db; --hover:#f9fafb;
            --color1:#2563eb; --color2:#059669; --color3:#7c3aed; --color4:#d946ef;
        }
        [data-theme="dark"] {
            --bg:#121212; --card:#1e1e1e; --title:#f9fafb; --text1:#f3f4f6; --text2:#e5e7eb; --text3:#d1d5db;
            --border:#333; --line:#444; --hover:#2d2d2d;
        }
        body { padding:30px; background:var(--bg); }
        .feature-tree-container {
            width:100%;
            margin:0 auto; background:var(--card);
            border-radius:18px; padding:32px; box-shadow:0 8px 28px rgba(0,0,0,0.08);
            border:1px solid var(--border);
        }
        .tool-bar {
            display:flex; align-items:center; justify-content:space-between;
            margin-bottom:24px; flex-wrap:wrap; gap:12px;
        }
        .tree-title { font-size:26px; font-weight:bold; color:var(--title); }
        .action-group { display:flex; gap:10px; }
        .btn {
            padding:8px 14px; border-radius:8px; border:none; cursor:pointer;
            font-size:14px; font-weight:500; display:flex; align-items:center; gap:6px;
            background:var(--hover); color:var(--text2);
        }
        .btn:hover { opacity:0.9; transform:translateY(-1px); }
        .btn-primary { background:#2563eb; color:white; }

        /* 版本标签 */
        .version-label {
            display:inline-block; margin:3px 4px 3px 0;
            font-size:9px;
            padding:2px 5px;
            border-radius:6px;
            font-weight:bold; white-space:nowrap;
        }
        .v-support { background:#ecfdf5; color:#067f4d; border:1px solid #a7f3d0; }
        .v-part { background:#fffbeb; color:#d97706; border:1px solid #fcd34d; }
        [data-theme="dark"] .v-support { background:#064e3b; color:#a7f3d0; }
        [data-theme="dark"] .v-part { background:#78350f; color:#fcd34d; }

        /* ===================== 核心修改 ===================== */
        /* 缩进缩小到 2/3：24px → 16px */
        .tree-node { list-style:none; padding-left:16px; position:relative; }
        .tree-root { padding-left:0; }

        .tree-item {
            display:flex; align-items:center; padding:4px 0;
            cursor:pointer; transition:all 0.25s ease; color:var(--text2);
            position:relative;
        }
        .tree-item:hover { background:var(--hover); border-radius:8px; padding-left:6px; }
        
        /* 三角按钮位置 */
        .toggle-btn {
            width:16px; height:16px; display:inline-flex; align-items:center; justify-content:center;
            margin-right:6px;
            font-size:10px; color:var(--text3); user-select:none; flex-shrink:0;
        }
        .toggle-btn.collapsed::after { content:"▶" }
        .toggle-btn.expanded::after { content:"▼" }
        .no-toggle { visibility:hidden; }

        /* 竖线保留（正常显示） */
        .tree-node::before {
            content:""; position:absolute; top:0; left:8px;
            width:1px; height:100%; background:var(--line);
            z-index:0;
        }

        /* ===================== 只去掉 横线 ===================== */
        .tree-item::before {
            display:none; /* 去掉水平横线 */
        }

        /* 根节点去掉竖线 */
        .tree-root>.tree-node::before { display:none; }

        .feature-name { 
            flex:1; display:flex; align-items:center; gap:8px;
            min-width:0;
            word-wrap:break-word;
        }
        .feature-versions {
            display:flex; gap:4px; flex-wrap:wrap; flex-shrink:1;
            margin-left:8px;
            max-width:60%;
        }
        .icon { width:16px; text-align:center; flex-shrink:0; }

        /* 层级字号 */
        .tree-root>.tree-node>.tree-item .feature-name { font-size:18px; font-weight:bold; color:var(--text1); }
        .tree-root>.tree-node>.tree-child>.tree-node>.tree-item .feature-name { font-size:16px; font-weight:500; color:var(--color1); }
        .tree-root>.tree-node:nth-child(2)>.tree-child>.tree-node>.tree-item .feature-name { color:var(--color2); }
        .tree-root>.tree-node:nth-child(3)>.tree-child>.tree-node>.tree-item .feature-name { color:var(--color3); }
        .tree-child .tree-child .tree-item .feature-name { font-size:15px; color:var(--text2); }
        .tree-child .tree-child .tree-child .tree-item .feature-name { font-size:14px; color:var(--text3); }
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

        <ul class="tree-root">
            
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn expanded "></span>
                    <span class="feature-name"><i class="fa-solid fa-cogs icon"></i>算子设计</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>精度设计</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>精度设计</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">精度设计</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>理论性能建模</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>理论性能建模</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">理论性能建模</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>模板库自动寻优</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>自动寻优</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持模板库自动寻优</span>
                    <div class="feature-versions"><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持搜索空间拓展</span>
                    <div class="feature-versions"><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持剪枝函数注册</span>
                    <div class="feature-versions"><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持模板库接入</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">基于建模的寻优过程自动剪枝</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">基于多个case的综合寻优策略</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">基于JIT的编译效率提升</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>性能分析</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">算子耗时展示</span>
                    <div class="feature-versions"><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">算力使用情况展示</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">带宽展示</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持与加速库进行性能比对</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">指导搜索空间拓展优化</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>精度比对</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持与加速库进行结果精度比对</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>辅助特性</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">算子名称筛选</span>
                    <div class="feature-versions"><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">L2Cache控制</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">预热控制</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">执行模式控制（图模式、单算子模式）</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">数据生成控制（分布策略）</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn expanded "></span>
                    <span class="feature-name"><i class="fa-solid fa-cogs icon"></i>算子开发</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>算子迁移</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>算子迁移</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">算子迁移</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>辅助编码</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>辅助编码</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">辅助编码</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>快捷调用</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>快捷调用</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">快捷调用</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD 310B / A3 / A5</span></div>
                </div>
            </li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>精度验证</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>精度验证</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">精度验证</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>功能验证</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>功能验证</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">功能验证</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn expanded "></span>
                    <span class="feature-name"><i class="fa-solid fa-cogs icon"></i>算子测试</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>精度测试</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>精度测试</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">精度测试</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn expanded "></span>
                    <span class="feature-name"><i class="fa-solid fa-cogs icon"></i>算子调试</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>在板调试</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>断点设置</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">普通断点</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">条件断点</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">地址断点</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3</span><span class="version-label v-part">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Kernel入口断点</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>程序执行控制</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Continue</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">SingleStep</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">StepOver</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">StepIn</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">StepOut</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">CTRL_C</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3</span><span class="version-label v-part">CATLASS A3</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>上下文切换</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">设备内上下文切换（核切换）</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">设备切换</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3</span><span class="version-label v-part">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">寄存器查询</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">上下文信息查询（核id等）</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">常量区域查询</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>内存访问</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">变量读</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">变量写</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">内存读</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">内存写</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Host程序侧读Device内存</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Host程序侧写Device内存</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>Coredump解析</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Coredump展示寄存器</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Coredump展示调用栈</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">Triton A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Coredump展示内存</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>辅助特性</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持attach进程方式调试</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">自动捕获并检查Host API错误码</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">自动捕获并检查硬件错误信息</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">自动单步执行定位异常代码</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">图模式支持(单流)</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">图模式支持(多流)</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Host程序调试能力</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>开放接口</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Initialzation API:初始化调试模式的API</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Device Execution Control API:控制硬件继续运行与单步执行</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Breakpoints API:控制断点的设置取消</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Device State Inspection API:查询Device上的内存等信息</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Device State Alteration API:用于修改Device上的内存等信息</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Properties API:硬件/程序属性查询</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">DWARF Utilities API: DWARF工具封装API</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Events: 标识硬件上报的各种事件</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>异常检测</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>Memcheck（内存检测）</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">内存非对齐对齐(Device)</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">内存越界访问检查(Device)</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">硬件异常上报(Device)</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">非法malloc/free使用检查（Device）</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Device malloc泄漏检查（Device）</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Api调用错误检查(Host)</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3 / A5</span><span class="version-label v-part">Triton A3 / A5</span><span class="version-label v-part">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Api调用错误检查(Device)</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Malloc GM内存泄露检查（Host）</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">连续buffer访问越界检测（Host/Device)</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Stream间竞争检测（Host）</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">内存踩踏检测（Device）</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>Racecheck（竞争检测）</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">流水间竞争检测</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">流水内竞争检测</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">核间竞争检测</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">cluster间共享内存竞争检测</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">卡间共享内存竞争检测</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>Initcheck（初始化检测）</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">读未初始化内存（Host）</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">读未初始化内存（Device）</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">Triton A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">申请但未使用内存检测（Host）</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">申请但未使用内存检测（Device）</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">Triton A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>Synccheck（同步检测）</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">同步语义死锁检测</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">同步语义使用错误检测（入参、调用位置等）</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">同步语义配对/冗余检测</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3</span><span class="version-label v-part">Triton A3</span><span class="version-label v-part">CATLASS A3</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>Overflowcheck（溢出检测）</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">数值计算溢出检测（Device）</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>辅助特性</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持控制并发or串行检测</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持Host异常点堆栈展示</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持Device异常点堆栈展示</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3 / A5</span><span class="version-label v-part">Triton A3 / A5</span><span class="version-label v-part">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持GPU动态并行任务的异常检测</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持程序结束时寄存器状态检测</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Kernel名称过滤</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">异常时可以生成core文件，用于调试器分析</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">识别到异常时动作（终止执行，继续执行）</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">误报抑制文件控制误报情况</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">免编译检测能力使能</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3 / A5</span><span class="version-label v-part">Triton A3 / A5</span><span class="version-label v-part">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">图模式支持</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3 / A5</span><span class="version-label v-part">Triton A3 / A5</span><span class="version-label v-part">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持进程attach方式检测</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>开放接口</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Memory API，支持用户替换CUDA API配合工具使用（Host）</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Callback API，支持用户在CUDA API上注册自己的回调（Host）</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Patching API，支持用户在Kernel内存操作上注册回调（Device）</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>TX拓展接口支持</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Suballocation API，支持程序向工具上报自规划内存池使用情况</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Naming API，支持对分配的内存进行标记</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Permissions API，支持对内存设置可读写属性</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Mark Initialized API，支持标记内存的初始化状态</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Kernel侧TX能力支持</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">Triton A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li></ul></li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn expanded "></span>
                    <span class="feature-name"><i class="fa-solid fa-cogs icon"></i>算子调优</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>在板调优</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>采集方式</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Kernel级重放</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Application级重放</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Range级重放</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>采集指标</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">内存负载分析</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">计算负载分析</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Roofline分析</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">通信拓扑分析</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">PMU采样分析</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">L2Cache命中统计</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">ICache命中统计</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">资源负载均衡分析</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">热点指令分析</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">算子流水轨迹分析</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A5</span><span class="version-label v-part">Triton A5</span><span class="version-label v-part">CATLASS A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">通算掩盖流水分析</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3 / A5</span><span class="version-label v-part">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">局部PMU数据分析</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">L2Cache热点建模分析</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">Triton A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>辅助特性</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">自动预热</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Cache控制</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">交互式调优</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">频率控制</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">性能报告比对</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Attach进程调优</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">图模式支持</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">调优报告评论</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Kernel筛选</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">CPU调用栈</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">任务完成后程序控制</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>开放接口</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">CUPTI采集控制接口</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Profiling报告解析接口</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">专家建议注册接口</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">可视化页面配置接口</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">资源利用率预测接口</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">python调优框架</span>
                    <div class="feature-versions"></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>TX拓展接口支持</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">支持基于TX接口的采集范围控制</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li></ul></li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-folder-open icon"></i>仿真调优</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>采集方式</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">基于仿真器采集程序性能数据</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD 310B / A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">上板执行过程中仿真局部算子</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3</span><span class="version-label v-support">Triton A3</span><span class="version-label v-support">CATLASS A3</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>采集指标</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">仿真指令流水图</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD 310B / A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">仿真带宽波形图</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">同步指令配对关联分析</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Scalar头开销展示</span>
                    <div class="feature-versions"></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">仿真代码热点分析</span>
                    <div class="feature-versions"><span class="version-label v-part">AscendC SIMD A3 / A5</span><span class="version-label v-part">Triton A3 / A5</span><span class="version-label v-part">CATLASS A3 / A5</span></div>
                </div>
            </li></ul></li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed "></span>
                    <span class="feature-name"><i class="fa-solid fa-list-check icon"></i>辅助特性</span>
                    <div class="feature-versions"></div>
                </div>
            <ul class="tree-child" style="display: none;">
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">Kernel筛选</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD 310B / A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li>
            <li class="tree-node">
                <div class="tree-item">
                    <span class="toggle-btn collapsed no-toggle"></span>
                    <span class="feature-name">任务完成后程序控制</span>
                    <div class="feature-versions"><span class="version-label v-support">AscendC SIMD 310B / A3 / A5</span><span class="version-label v-support">Triton A3 / A5</span><span class="version-label v-support">CATLASS A3 / A5</span></div>
                </div>
            </li></ul></li></ul></li></ul></li>
        </ul>
    </div>

    <script>
        document.querySelectorAll('.toggle-btn').forEach(btn=>{
            btn.addEventListener('click',e=>{
                e.stopPropagation()
                const child = btn.closest('.tree-item').nextElementSibling;
                if(!child) return;
                const hide = child.style.display === 'none';
                child.style.display = hide ? 'block' : 'none';
                btn.classList.toggle('collapsed',!hide);
                btn.classList.toggle('expanded',hide);
            })
        })
        document.getElementById('expandAll').onclick=()=>{
            document.querySelectorAll('.tree-child').forEach(c=>c.style.display='block');
            document.querySelectorAll('.toggle-btn').forEach(b=>{b.className='toggle-btn expanded'});
        }
        document.getElementById('collapseAll').onclick=()=>{
            document.querySelectorAll('.tree-child').forEach(c=>c.style.display='none');
            document.querySelectorAll('.toggle-btn').forEach(b=>{
                if(!b.classList.contains('no-toggle')) b.className='toggle-btn collapsed';
            })
        }
        document.getElementById('toggleDark').onclick=()=>{
            const isDark = document.documentElement.dataset.theme === 'dark';
            if(isDark) {
                document.documentElement.removeAttribute('data-theme');
                this.innerHTML='<i class="fa-solid fa-moon"></i> 暗黑模式';
            }else{
                document.documentElement.dataset.theme='dark';
                this.innerHTML='<i class="fa-solid fa-sun"></i> 明亮模式';
            }
        }
    </script>
</body>
</html>