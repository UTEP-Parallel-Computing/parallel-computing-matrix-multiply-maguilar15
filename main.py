from matrixUtils import *
import os
#Debugger
import numpy as np

# Check Time
import time

def makeReport(cpuModelName:str=None,matrixSize:int=8, matrixValue:int=1,thread_test:list=[1,2,4,8,16]):
    A = genMatrix(matrixSize, matrixValue)
    B = genMatrix(matrixSize, matrixValue)

    template = lambda m,t,s: f"""| {cpuModelName} | {m}x{m} | {t} | {s} |"""

    for num_threads in thread_test:
        startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        parallelMultiplyMatrix(A, B, num_threads=num_threads)
        endTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        elapsedTime = endTime - startTime
        #print(f"Number of Threads={t} Time Elapsed: {endTime - startTime}")
        time.sleep(1)
        print(template(matrixSize,num_threads,elapsedTime))

def makeCSVReport(cpuModelName:str=None, matrixSize:int=8, matrixValue:int=1, thread_test:list=[1, 2, 4, 8, 16]):
    A = genMatrix(matrixSize, matrixValue)
    B = genMatrix(matrixSize, matrixValue)

    template = lambda m, t, s: f"""{cpuModelName},{m},{t},{s}"""

    for num_threads in thread_test:
        startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        parallelMultiplyMatrix(A, B, num_threads=num_threads)
        endTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        elapsedTime = endTime - startTime
        # print(f"Number of Threads={t} Time Elapsed: {endTime - startTime}")
        time.sleep(1)
        print(template(matrixSize, num_threads, elapsedTime))


if __name__ == "__main__":


    cpuModel = os.getenv("CPUMODEL") if os.getenv("CPUMODEL") else "Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz"

    # Size for Matrix multiply
    #testMatrixSize = [8,16,32,64,128,256,512,1024,2048,4096]
    testMatrixSize = [8, 16, 32, 64,128,256]
    # Threads to execute in parallel
    thread_test = [1, 2, 4, 8, 16, 32]

    #columnsNames = f"""| CPU INFO | Matrix Size | Threads Size | Seconds Elapsed |\n|----------|-------------|:---------|:---------------|"""
    columnsNames = f"""CPU INFO,Matrix Size,Threads Size,Seconds Elapsed"""
    print(columnsNames)
    for e in testMatrixSize:
        makeCSVReport(cpuModelName=cpuModel,matrixSize=e,matrixValue=100,thread_test=thread_test)
