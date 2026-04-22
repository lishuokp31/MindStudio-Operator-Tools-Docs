# MindStudio-Operator-Tools-Docs

MindStudio-Operator-Tools 文档托管仓库

本仓库用于整合 MindStudio-Operator-Tools 算子开发工具相关文档，并通过 MkDocs统一对外提供站点。

当前整合的子工具包括：


| 类别 | 工具名称 | 功能简介                                                      |
|:--:| :--- |:----------------------------------------------------------|
| 设计 | [**msKPP**](https://gitcode.com/Ascend/mskpp) | **【性能预测】** 支持输入算子描述，预测算子在特定算法实现下的性能上限。                    |
| 构建 | [**msOpGen**](https://gitcode.com/Ascend/msopgen) | **【工程生成】** 算子开发效率提升工具，提供模板工程生成能力，简化工程搭建。                  |
| 验证 | [**msKL**](https://gitcode.com/Ascend/mskl) | **【快捷调用】** 提供 Python 接口，快速实现 Kernel 的下发运行，便于快速完成功能验证。         |
| 检测 | [**msSanitizer**](https://gitcode.com/Ascend/mssanitizer) | **【异常检测】** 提供内存、竞争、未初始化及同步检测，支持多核程序内存问题的精准定位。             |
| 调试 | [**msDebug**](https://gitcode.com/Ascend/msdebug) | **【原生调试】** 基于昇腾处理器的原生环境调试，支持变量查看、单步执行及上板调试。               |
| 调优 | [**msOpProf**](https://gitcode.com/Ascend/msopprof) | **【性能分析】** 支持上板与仿真数据采集，通过 MindStudio Insight 可视化工具定位性能瓶颈。 |

## 目录说明

```text
.
├── readthedocs/
│   ├── docs/                 # MkDocs 文档根目录
│   ├── mkdocs.yml            # MkDocs 配置
│   ├── requirements.txt      # 文档依赖
│   └── scripts/build_docs.py # 预构建脚本：同步子工具文档并生成导航
├── .readthedocs.yaml         # Read the Docs 构建配置
└── .gitmodules               # 子模块配置
```

## 本地准备

建议使用 Python 3.10+。

先拉取仓库和子模块：

```bash
git clone --recurse-submodules <repo-url>
cd mindstudio-profiler-docs
git submodule sync --recursive
git submodule update --init --recursive --depth=1
git submodule update --remote --recursive
```

安装文档依赖：

```bash
python3 -m pip install -r readthedocs/requirements.txt
```

## 本地启动服务

本地预览前需要先执行一次预构建脚本。这个脚本会：

- 从各子工具仓库同步文档
- 过滤需要展示的目录与页面
- 生成工具导航与首页入口
- 重写部分站内链接

执行命令：

```bash
python3 readthedocs/scripts/build_docs.py
```

然后启动本地服务：

```bash
mkdocs serve -f readthedocs/mkdocs.yml -a 127.0.0.1:8000
```

启动后浏览器访问：

```text
http://127.0.0.1:8000
```

如果 `8000` 端口已被占用，可以改成别的端口，例如：

```bash
mkdocs serve -f readthedocs/mkdocs.yml -a 127.0.0.1:8001
```

## 本地构建

如果只想检查能否成功构建静态站点，可以执行：

```bash
python3 readthedocs/scripts/build_docs.py
mkdocs build -f readthedocs/mkdocs.yml --strict
```

构建产物默认输出到：

```text
readthedocs/site/
```










