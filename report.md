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
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 1 | 0.01935273300000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 2 | 0.02208032900000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 4 | 0.015130809000000023 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 8 | 0.032300474999999995 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 1 | 0.020920890999999997 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 2 | 0.018518461000000097 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 4 | 0.019167914000000064 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 8 | 0.024317849000000002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 1 | 0.059165154 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 2 | 0.021561559000000008 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 4 | 0.020462897000000035 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 8 | 0.01946179800000003 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 1 | 0.37718214399999983 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 2 | 0.10137511900000007 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 4 | 0.024953859000000023 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 8 | 0.019453603999999958 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 1 | 2.389094666 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 2 | 0.31378337000000034 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 4 | 0.09945962100000028 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 8 | 0.06227790300000002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 1 | 15.187745129 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 2 | 2.7682572090000015 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 4 | 0.521877915000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 8 | 0.09967445999999924 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 1 | 142.93426319600002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 2 | 17.63808076000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 4 | 3.839328848000008 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 8 | 0.5130418260000056 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 1024x1024 | 1 | 1202.130515153 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 1024x1024 | 2 | 174.22838992300012 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 1024x1024 | 4 | 30.20789825399993 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 1024x1024 | 8 | 3.8935794289998285 |





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

| CPU INFO | Matrix Size | Threads Size | Seconds Elapsed |
|---|---|:---|:---|
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 1 | 0.01935273300000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 2 | 0.02208032900000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 4 | 0.015130809000000023 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 8 | 0.032300474999999995 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 16 | 0.033089586000000004 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 32 | 0.06306674099999998 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 1 | 0.020920890999999997 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 2 | 0.018518461000000097 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 4 | 0.019167914000000064 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 8 | 0.024317849000000002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 16 | 0.04296222599999999 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 32 | 0.06399386900000004 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 1 | 0.059165154 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 2 | 0.021561559000000008 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 4 | 0.020462897000000035 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 8 | 0.01946179800000003 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 16 | 0.035281974000000105 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 32 | 0.06398661800000005 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 1 | 0.37718214399999983 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 2 | 0.10137511900000007 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 4 | 0.024953859000000023 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 8 | 0.019453603999999958 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 16 | 0.030611208000000056 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 32 | 0.041937219000000026 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 1 | 2.389094666 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 2 | 0.31378337000000034 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 4 | 0.09945962100000028 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 8 | 0.06227790300000002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 16 | 0.04453403399999978 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 32 | 0.05645749500000008 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 1 | 15.187745129 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 2 | 2.7682572090000015 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 4 | 0.521877915000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 8 | 0.09967445999999924 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 16 | 0.04365383899999742 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 32 | 0.049693118000000425 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 1 | 142.93426319600002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 2 | 17.63808076000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 4 | 3.839328848000008 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 8 | 0.5130418260000056 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 16 | 0.10226080999998999 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 32 | 0.07304471699998771 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 1024x1024 | 1 | 1202.130515153 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 1024x1024 | 2 | 174.22838992300012 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 1024x1024 | 4 | 30.20789825399993 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 1024x1024 | 8 | 3.8935794289998285 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 1024x1024 | 16 | 0.5429076390000773 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 1024x1024 | 32 | 0.14854856900001323 |


