## Parallel Computing Matrix Multiply Assignment

This repository contains some basic Python utilities for
matrix operations. This is also the repository where
you will submit the assignment.

Once completed the repository should contain your code,
a short report, and any instructions needed to run your
code.

## Execute Program 

### Environment Variables 
* CPUMODEL
    * The CPU model of the computer running this program. You can find CPU information by running the **cpuinfo.sh** script.  
* REPORT
    * Setting environment variable to 0 will return a markdown table with all computed results. Setting it to 1 will return a CSV file containing the same results. 

#### Example 

```bash 
export CPUMODEL="Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz"
 
export REPORT=0 

python main.py 
```

##### Save Results 

```bash 
python main.py > results.txt
```