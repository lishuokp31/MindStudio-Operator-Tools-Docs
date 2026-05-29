# MindStudio Sanitizer 算子卡死检测样例介绍

## 概述

本样例演示如何使用 **mssanitizer** 工具对算子进行卡死异常检测和定位。

## 适用场景

- 算子执行时间异常超出预期，持续不结束，疑似存在死锁或同步等待。
- 需要快速定位算子内部异常同步指令的代码位置。

## 支持的产品范围

- Ascend 950PR/Ascend 950DT
- Atlas A3 训练系列产品/Atlas A3 推理系列产品
- Atlas A2 训练系列产品/Atlas A2 推理系列产品

## 目录结构

```
├── stuck_check/
│   ├── kernel.cpp      # 算子 kernel 侧实现（含卡死异常）
│   ├── main.cpp        # 算子 host 侧实现
│   ├── Makefile        # 编译工程文件
│   └── README.md       # 本说明文件
```

## 样例描述

### 核心逻辑

本样例在 `kernel.cpp` 中实现了一个基础的搬入-搬出（DataCopy）算子，其正常执行流程为：

1. 将 Global Memory 中的输入数据搬入 Local Memory（`DataCopy(xLm, xGm, 256)`）。
2. 将 Local Memory 中的结果数据搬回 Global Memory（`DataCopy(xGm, xLm, 256)`）。

### 注入异常

在上述两步搬运操作之间，刻意插入了一条**孤立且未配对**的 `wait_flag` 指令：

```cpp
wait_flag(PIPE_V, PIPE_MTE2, EVENT_ID0);
```

由于整个算子中不存在与之对应的 `set_flag(PIPE_MTE2, EVENT_ID0)` 调用，该 `wait_flag` 将永久等待一个永远不会到达的事件，导致 PIPE_MTE2 流水线陷入死锁，算子无法继续执行后续的 `DataCopy(xGm, xLm, 256)`，表现为卡死。

## 编译运行

### 环境准备

请参照官方文档完成开发环境配置：[算子工具开发环境安装指导](https://gitcode.com/Ascend/msot/blob/master/docs/zh/common/dev_env_setup.md)。

### 编译算子

在 `stuck_check/` 目录下执行：

```bash
make -j
```

编译完成后，当前目录将生成算子二进制文件 `test.fatbin`。

> **说明**：Makefile 中已包含 `--cce-enable-sanitizer` 编译选项，用于启用 sanitizer 检测所需的调试信息。若需检测自己的算子，请确保在编译参数中增加 `-g --cce-enable-sanitizer`。

### 算子运行

1.拉起算子： 
使用 mssanitizer 工具，指定 synccheck 模式拉起算子：

```bash
mssanitizer -t synccheck test.fatbin
```

> **说明**：mssanitizer命令参数含义请参考：[mssanitizer 用户指南](https://www.hiascend.com/document/detail/zh/canncommercial/900/devaids/optool/docs/zh/user_guide/mssanitizer_user_guide.md)。

工具成功拉起算子后，将在终端输出如下日志：

```
[mssanitizer] logging to file: ./mindstudio_sanitizer_log/mssanitizer_XXX.log
[mssanitizer] Start synccheck sanitizer on kernel kernel
```

2. 手动终止算子运行
由于 `wait_flag` 指令的存在，算子将在该处阻塞。此时需按下 `Ctrl+C` 手动终止算子进程：

```
^CCtrl-C received. Running kernel will be killed, and you can press Ctrl-C again to force quit.
```

3. 检测报告分析：

工具捕获退出信号后，分析同步状态并输出卡死诊断报告：

```
====== ERROR: Sync error detected. kernel locked up at
======
======    WAIT_FLAG in kernel
======    by PIPE_MTE2 in block aiv(0) on device 1
======    code in pc current 0xf0c (serialNo:13)
======    #0 /XXX/kernel.cpp:18:5
======
====== SUMMARY: 1 pipe(s) locked up.
```

根据诊断报告，可以确认 `kernel.cpp` 第 18 行（即 `wait_flag`）为卡死根因。修复方式为删除该孤立指令，或为其添加对应的 `set_flag` 调用。

## 检测流程总结

1. 拉起算子 mssanitizer -t synccheck XXX
2. 算子卡死后手动 Ctrl+C 终止算子进程
3. 分析诊断报告，定位源码异常行并修复

## 注意事项
- 检测自定义算子前，请确认编译选项中包含 `-g --cce-enable-sanitizer`，否则无法使用工具检测能力。
