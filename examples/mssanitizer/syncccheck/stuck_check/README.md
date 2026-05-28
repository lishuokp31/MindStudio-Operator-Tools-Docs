# MindStudio Sanitizer 算子卡死检测样例介绍

## 概述

本样例介绍使用mssanitizer检测工具进行算子卡死异常检测。

## 适用场景

- 算子因同步指令异常导致卡死场景、或执行时间过长不结束。可快速定位

## 支持的产品范围

- Ascend 950PR/Ascend 950DT
- Atlas A3 训练系列产品/Atlas A3 推理系列产品
- Atlas A2 训练系列产品/Atlas A2 推理系列产品

## 目录结构介绍
```
├── stuck_check
│   ├── kernel.cpp                  // 卡死算子实现-kernel侧
│   ├── main.cpp                    // 卡死算子实现-host侧
│   ├── Makefile                    // 编译工程文件
│   └── README.md                   // 说明文件
```

## 样例描述

- kernel.cpp中实现了一个非常简单的搬入-搬出算子，但操作流程中有一个独立未配对的wait_flag命令。该命令会导致算子卡死。
- 通过使用mssanitizer工具的同步检测功能，可以检测出算子异常，并提示造成卡死的代码位置。

## 编译运行

请在本样例根目录下执行如下步骤：

1. 环境准备

    请按照以下文档进行环境配置：《[算子工具开发环境安装指导](https://gitcode.com/Ascend/msot/blob/master/docs/zh/common/dev_env_setup.md)》。

2. 样例执行

    - 在前目录下执行以下命令编译算子：

        ```
        make -j
        ```

    - 编译完成后，可以在当前目录下看到生成的算子二进制文件test.fatbin。使用检测工具、指定检测类型为synccheck执行算子：
    
        ```
        mssanitizer -t synccheck test.fatbin
        ```

        命令解析：

        - mssanitizer：算子检测工具关键字
        - -t：指定mssanitizer要执行的检测模式。更多用法可参考[昇腾社区相关文档](https://www.hiascend.com/document/detail/zh/canncommercial/900/devaids/optool/docs/zh/user_guide/mssanitizer_user_guide.md)。
        - synccheck：指定使用同步检测功能
        - test.fatbin：被检测的算子二进制

    - 工具拉起算子后，会打印开始监测日志信息：
        ```
        [mssanitizer] logging to file: ./mindstudio_sanitizer_log/mssanitizer_XXX.log
        [mssanitizer] Start synccheck sanitizer on kernel kernel
        ```
        此时由于异常同步指令wait_flag的存在，算子执行会在此处卡死。**此时需要在键盘上按下ctrl-c手动终止算子运行**，随后可以看到算子退出提示：
        ```
        ^CCtrl-C received. Running kernel will be killed, and you can press Ctrl-C again to force quit.
        ```
        之后工具会检测算子异常，并输出卡死告警信息：
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
    - 从工具输出的卡死告警信息中可以确认：kernel.cpp的第18行代码导致了异常卡死，从源文件中确认我们可以直接定位异常的wait_flag指令并进行修改。

## 总结

算子卡死检测三步走策略：
1. 使用检测工具拉起算子，执行至卡死位置。
2. 键盘ctrl-c手动终止算子运行。
3. 查看工具输出的卡死告警，确认源码问题位置。


## 其他说明

- 使用该功能检测自定义算子时，请确保为算子编译工程增加如下编译参数并重新编译后，再使用检测工具拉起检测：
```
-g --cce-enable-sanitizer
```