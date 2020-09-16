# Parallel Matrix Multiply Report 
Manuel Aguilar

### What problems you encountered completing the assignment and how you overcame them 

Learning the library **pymp** is challenging because it is a different way of writing code. As a beginner, programs have been written sequentially. This assignments shows how to write a parallel algorithm utilizing all cores available on the machine. 
Using the **pymp** library allows for writing parallel programs.      
Performing parallel operations must be inside a **with** block in python. This limits the scoping of variables accessible outside the **with** block.  
Installing the **pymp** library was not as challenging as I thought. I was able to recreate the *parallel computing VM* using pip inside my python environment.
 

### Any problems you weren't able to overcome or any bugs still left in the program 

No problems were encountered with the lab. The parallel matrix algorithm does produce the correct result. 
This can be verified by using the **numpy** matrix multiplier function to compare results. 

### About how long it took you to complete the assignment 

It took me three days to complete the assignment. I first had to import the **pymp** library and learn the syntax. 
This was required to write a parallel version of a sequential matrix multiply algorithm. 
I started by configuring my host machine to use the **pymp** library using pip. 
After installing **pymp** I did the class examples on [Github](https://github.com/daviddpruitt/Pymp_examples) 
in combination with the notes on the **pymp** project's [Github](https://github.com/classner/pymp) page.
Finally, it was to complete the report demonstrating the results on my CPU.  


### Performance measurements (given in seconds) for 1, 2, 4, and 8 threads 

| CPU INFO | Matrix Size | Threads Size | Seconds Elapsed |
|---|---|:---|:---|
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 1 | 0.011868518999999994 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 2 | 0.025971787999999996 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 4 | 0.033824671 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 8 | 0.033964949999999966 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 1 | 0.03326378399999996 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 2 | 0.02069426499999999 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 4 | 0.02554685200000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 8 | 0.015176995000000026 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 1 | 0.05793319999999991 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 2 | 0.04069257000000004 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 4 | 0.02803959300000003 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 8 | 0.029031126000000018 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 1 | 0.24680522800000004 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 2 | 0.061658447000000116 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 4 | 0.025049045999999908 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 8 | 0.016954343999999955 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 1 | 1.976558742 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 2 | 0.25249154399999973 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 4 | 0.16492167000000002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 8 | 0.027944489999999877 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 1 | 13.487017875 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 2 | 2.0609505319999997 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 4 | 0.5757090969999972 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 8 | 0.11748792399999886 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 1 | 112.82246569800002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 2 | 14.897171364000002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 4 | 3.6639741500000014 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 8 | 0.5292462869999781 |



### A short analysis of why the program behaves as it does with an increasing number of threads 

The parallel matrix multiply algorithm works because I cross referenced it with the **numpy** matrix multiplier function. 
This was to ensure the parallel algorithm did provide the correct result. Increasing the thread size on large matrices does reduce the time to complete. 
However, in some cases the parallel algorithm does not improve if more threads are being used. This can be seen in the table when multiplying small matrices with multiple threads. 

### Any observations or comments you had while doing the assignment 

In some cases the matrix multiply algorithm in parallel does not improve speed up completion if more threads are used. 
This can be seen in the table when multiplying small matrices with multiple threads.

### Output from the cpuInfoDump.sh program  

```
model name      : Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz
      4      36     216
```

## Table Report

