---
hide:
  - navigation
  - toc
---


# 算子工具全景

## 算子工具链

<style>
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
</style>

<!-- <div class="ai-arch-container">
    <div class="arch-wrapper" id="container">
        <div class="main-layers">
            <div class="layer-section">
                <div class="layer-title">分析工具</div>
                <div class="layer-content">
                    <div class="module" data-title="msprof-analyze" data-desc="面向 AI 训练与推理场景的性能分析工具，具备性能比对、集群分析、专家建议等功能。">
                        msprof-analyze
                    </div>
                    <div class="module" data-title="msAgent" data-desc="专注于性能问题定位的Agent。">
                        msAgent
                    </div>
                </div>
            </div>

            <div class="layer-section">
                <div class="layer-title">性能监控</div>
                <div class="layer-content">
                    <div class="module span-2 flex-center" data-title="msMonitor" data-desc="面向昇腾集群场景的在线性能监控与动态采集工具。">
                        MindStudio Monitor
                    </div>
                </div>
            </div>

            <div class="layer-section">
                <div class="layer-title">AI框架</div>
                <div class="layer-content justify-content-around">
                    <div class="module" data-title="PyTorch Profiler" data-desc="基于PyTorch框架开发的昇腾软硬件性能调优工具。">PyTorch Profiler</div>
                    <div class="module" data-title="MindSpore Profiler" data-desc="基于昇思MindSpore框架开发的昇腾软硬件性能调优工具。">MindSpore Profiler</div>
                </div>
            </div>

            <div class="layer-section">
                <div class="layer-title">基础能力</div>
                <div class="layer-content layer-content-3">
                    <div class="module" data-title="msProf" data-desc="昇腾Profiling命令行工具，支持采集与解析 CANN 平台及昇腾 AI 处理器的软硬件性能数据。">msProf</div>
                    <div class="module" data-title="MSTX" data-desc="MindStudio Tools Extension Library，支持用户自定义打点。">MSTX</div>
                    <div class="module" data-title="MSPTI" data-desc="MindStudio Profiler Tools Interface，面向昇腾设备的 Profiling API 集合。">MSPTI</div>
                </div>
            </div>
        </div>

        <div class="tool-card" data-title="MindStudio Insight" data-desc="全流程可视化性能分析套件，支持 Timeline、算子清单及智能瓶颈定位。">
            MindStudio Insight
        </div>

        <div id="dynamic-preview">
            <div class="preview-h" id="pre-title"></div>
            <p class="preview-p" id="pre-desc"></p>
        </div>
    </div>
</div> -->

<!-- <script>
(function () {
    const targetHrefMap = {
        'msprof-analyze': '../msprof-analyze/',
        'MindStudio Insight': '../msinsight/',
        'msAgent': '../msagent/',
        'msMonitor': '../msmonitor/',
        'PyTorch Profiler': '../torch_npu_profiler/',
        'MindSpore Profiler': 'https://www.mindspore.cn/mindinsight/docs/zh-CN/r2.3/performance_profiling_ascend.html',
        'msProf': '../msprof/',
        'MSTX': 'https://gitcode.com/Ascend/mstx',
        'MSPTI': '../mspti/'
    };

    function initToolchainMap() {
        const arch = document.querySelector('.ai-arch-container');
        if (!arch || arch.dataset.initialized === 'true') {
            return;
        }

        arch.dataset.initialized = 'true';

        const preview = arch.querySelector('#dynamic-preview');
        const pTitle = arch.querySelector('#pre-title');
        const pDesc = arch.querySelector('#pre-desc');
        const container = arch.querySelector('#container');
        const targets = arch.querySelectorAll('.module, .tool-card');

        if (!preview || !pTitle || !pDesc || !container || !targets.length) {
            return;
        }

        const hidePreview = () => {
            preview.classList.remove('active');
        };

        const showPreview = (target) => {
            if (window.innerWidth <= 850) {
                return;
            }

            pTitle.innerText = target.getAttribute('data-title') || '';
            pDesc.innerText = target.getAttribute('data-desc') || '';

            const rect = target.getBoundingClientRect();
            const containerRect = container.getBoundingClientRect();

            preview.style.top = (rect.top - containerRect.top) + 'px';
            preview.style.left = (rect.right - containerRect.left + 15) + 'px';
            preview.classList.add('active');
        };

        const navigateToTarget = (target) => {
            const title = target.getAttribute('data-title') || '';
            const href = targetHrefMap[title];
            if (!href) {
                return;
            }

            window.location.assign(href);
        };

        container.addEventListener('mouseleave', hidePreview);

        targets.forEach((target) => {
            target.setAttribute('role', 'link');
            target.setAttribute('tabindex', '0');

            target.addEventListener('mouseenter', () => showPreview(target));
            target.addEventListener('focus', () => showPreview(target));
            target.addEventListener('mouseleave', hidePreview);
            target.addEventListener('blur', hidePreview);
            target.addEventListener('click', () => navigateToTarget(target));
            target.addEventListener('keydown', (event) => {
                if (event.key === 'Enter' || event.key === ' ') {
                    event.preventDefault();
                    navigateToTarget(target);
                }
            });
        });
    }

    if (typeof document$ !== 'undefined' && typeof document$.subscribe === 'function') {
        document$.subscribe(initToolchainMap);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initToolchainMap, { once: true });
    } else {
        initToolchainMap();
    }
})();
</script> -->

![profiling-data](../assets/images/fullview.svg)

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

