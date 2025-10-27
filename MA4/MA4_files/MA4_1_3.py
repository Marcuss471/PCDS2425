
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
from time import perf_counter as pc
import concurrent.futures as future

def insideSphere(a):
    if sum(a) <= 1:
        return True
    else:
        return False

def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere 
    # sidan upphöjt till dimensioner
    power = lambda a : a*a      #Lambda
    coordinates = [[power(r.uniform(-1, 1)) for i in range(d)] for i in range(n)]       #List comprehension
    
    tempFilter = filter(insideSphere, coordinates)    #Use of filter
    LenInsideSphere = len([i for i in tempFilter])

    volumeSquare = 2**d     # -1 to 1 is 2.
    
    return (volumeSquare*(LenInsideSphere/n))

def hypersphere_exact(n,d):
    return (m.pi**(d/2))/(m.gamma((d/2)+1))

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    # using multiprocessor to perform 10 iterations of volume function  
    # n_split = [int(n/np) for i in range(np)]
    # d_split = [int(d/np) for i in range(np)]
    n_split = [n for i in range(np)]
    d_split = [d for i in range(np)]
    
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, n_split, d_split)
    
    return sum(results)/np

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
    n_split = [int(n/np) for i in range(np)]
    d_split = [d for i in range(np)]
    
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, n_split, d_split)
    
    return sum(results)/np

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 10     # 10 process to be executed
    
    # Parallel 1
    start = pc()
    print(sphere_volume_parallel1(n, d, np))
    end = pc()
    print(f'parallel1 finished in {round(end-start, 2)}s')

    # Parallel 2
    start = pc()
    print(sphere_volume_parallel1(n, d, np))
    end = pc()
    print(f'parallel2 finished in {round(end-start, 2)}s')
    
    # Regular
    start = pc()
    lst = []
    for y in range(np):
        lst.append(sphere_volume(n,d))
    end = pc()
    print(sum(lst)/np)
    print(f'regular finished in {round(end-start, 2)}s')
    


if __name__ == '__main__':
	main()
