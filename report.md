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
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 1 | 0.010828265999999975 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 2 | 0.010046484999999994 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 4 | 0.023513231999999995 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 8 | 0.029343247000000017 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 1 | 0.018928719000000038 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 2 | 0.02868046599999996 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 4 | 0.02862620499999996 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 8 | 0.034399605 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 1 | 0.06194527300000002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 2 | 0.023594197999999955 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 4 | 0.02682574999999998 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 8 | 0.04629820799999995 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 1 | 0.2725266780000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 2 | 0.13718226099999997 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 4 | 0.13450676000000006 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 8 | 0.0985285039999999 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 1 | 2.109247962 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 2 | 0.9263108939999998 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 4 | 0.9765965110000003 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 8 | 0.49822008199999956 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 1 | 13.221513334 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 2 | 6.793992687000003 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 4 | 7.269498545999998 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 8 | 3.619597339000002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 1 | 110.51378800200001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 2 | 58.89956043999999 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 4 | 57.26949505900001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 8 | 29.019136984 |

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
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 1 | 0.010556916999999999 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 2 | 0.02669347800000002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 4 | 0.009981931999999999 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 8 | 0.013446069000000005 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 16 | 0.049041780000000035 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 8x8 | 32 | 0.03457135299999997 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 1 | 0.03646762199999998 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 2 | 0.014778803999999979 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 4 | 0.013232118000000015 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 8 | 0.036491123000000014 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 16 | 0.049683435 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 16x16 | 32 | 0.036155194 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 1 | 0.04540552600000003 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 2 | 0.04860575300000003 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 4 | 0.05237982000000008 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 8 | 0.042521586 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 16 | 0.045538458000000004 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 32x32 | 32 | 0.05890700500000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 1 | 0.21193443099999987 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 2 | 0.13941427000000006 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 4 | 0.11940901599999987 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 8 | 0.07806673600000003 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 16 | 0.07742633300000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 64x64 | 32 | 0.05222821100000008 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 1 | 1.6624480879999997 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 2 | 0.8999922839999996 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 4 | 0.9970044419999997 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 8 | 0.5156002190000004 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 16 | 0.2873140249999997 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 128x128 | 32 | 0.18146975799999954 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 1 | 13.544607037000002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 2 | 7.237210725000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 4 | 7.100438264000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 8 | 3.6296961289999956 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 16 | 1.791067634000001 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 256x256 | 32 | 0.9518804379999963 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 1 | 106.260488923 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 2 | 54.761144580999996 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 4 | 57.01952412000003 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 8 | 28.710645114000044 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 16 | 14.37548831700002 |
| Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz | 512x512 | 32 | 7.238106158999983 |

