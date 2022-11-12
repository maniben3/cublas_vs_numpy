#include <stdio.h>
#include <assert.h>
#include <cuda.h>
#include <cuda_runtime.h>


__global__ void test(){
    printf("Hi Cuda World");
}
void myprint(void);

int myprint()
{
    test<<<1,1>>>();
    cudaDeviceSynchronize();
    return printf("Hicuda");
}
