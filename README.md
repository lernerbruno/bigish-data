# Big-ish data
Workshop with Mike Tebeka

### Parallelism vs Concurrency
You can have 1 worker doing a lot of stuff at the same time -> this is Concurrency  
You can have a lot of workers doing stuff at the same time -> this is Parallelism  
Rob Pike: https://www.youtube.com/watch?v=cN_DpYBzKso

But there is a point where you just can't parallelize (e.g. wine making - you have to wait for it to be ready at some 
point in the process)  
#### Amdahl's Law  
https://en.wikipedia.org/wiki/Amdahl%27s_law

#### Joblib
https://joblib.readthedocs.io/en/latest/

###HDF5
It's a file format that behaves as a storage for big matrices.
It works as a dict where the values are DataFrames

