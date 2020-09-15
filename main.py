from matrixUtils import *

import os
# Check Time
import time
#Debugger
import numpy as np


def makeReport(template,cpuModelName:str=None, matrixSize:int=8, matrixValue:int=1, thread_test:list=[1, 2, 4, 8, 16]):
    A = genMatrix(matrixSize, matrixValue)
    B = genMatrix(matrixSize, matrixValue)

    for num_threads in thread_test:
        startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        parallelMultiplyMatrix(A, B, num_threads=num_threads)
        endTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
        elapsedTime = endTime - startTime
        time.sleep(1)
        print(template(cpuModelName,matrixSize,num_threads,elapsedTime))

if __name__ == "__main__":

    markdownTemplate = lambda c, m, t, s: f"""| {c} | {m}x{m} | {t} | {s} |"""
    csvTemplate = lambda c, m, t, s: f"""{c},{m},{t},{s}"""

    templates = {0:markdownTemplate,1:csvTemplate}

    cpuModel = os.getenv("CPUMODEL") if os.getenv("CPUMODEL") else "Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz"
    # 0:markdown ^ 1:CSV
    reportType = os.getenv("REPORT") if os.getenv("REPORT") else 0

    # Size for Matrix multiply
    #testMatrixSize = [8,16,32,64,128,256,512,1024,2048,4096]
    testMatrixSize = [8, 16, 32, 64, 128, 256, 512]
    # Threads to execute in parallel
    thread_test = [1, 2, 4, 8, 16, 32]

    if reportType:
        columnsNames = f"""CPU INFO,Matrix Size,Threads Size,Seconds Elapsed"""
    else:
        columnsNames = f"""| CPU INFO | Matrix Size | Threads Size | Seconds Elapsed |\n|---|---|:---|:---|"""

    print(columnsNames)
    for e in testMatrixSize:
        makeReport(template=templates[reportType],cpuModelName=cpuModel,matrixSize=e,matrixValue=100,thread_test=thread_test)
