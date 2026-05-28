#include "kernel_operator.h"
#include "acl/acl.h"
using namespace AscendC;

extern "C" __global__ __aicore__ void kernel(__gm__ uint8_t *gmDeviceInput, __gm__ uint8_t *gmDeviceOutput)
{
    TPipe pipe;
    TBuf<QuePosition::VECCALC> xlm;
    GlobalTensor<uint8_t> xGm;
    pipe.InitBuffer(xlm, 256);
    LocalTensor<uint8_t> xLm = xlm.Get<uint8_t>();
    xGm.SetGlobalBuffer((__gm__ uint8_t *)gmDeviceInput, 256);

    // UB基本搬运操作
    DataCopy(xLm, xGm, 256);

    // WAIT_FLAG 没有对应的 SET_FLAG，卡死
    wait_flag(PIPE_V, PIPE_MTE2, EVENT_ID0);

    // 执行不到这里
    DataCopy(xGm, xLm, 256);
}

extern "C" void kernel_do(uint32_t blockDim, void *l2ctrl, void *stream, uint8_t *gmDeviceInput, uint8_t *gmDeviceOutput)
{
    kernel<<<blockDim, l2ctrl, stream>>>(gmDeviceInput, gmDeviceOutput);
}