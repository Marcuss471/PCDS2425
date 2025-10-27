
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r

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

def hypersphere_exact(d):
    return (m.pi**(d/2))/(m.gamma((d/2)+1))
     
def main():
    n = 100000
    d = 2
    print(f'Approximation of pi in {d} dimensons, when n = {n}:\t {sphere_volume(n,d)}')
    print(f'Exact value of pi in {d} dimensions:\t\t\t {hypersphere_exact(d)}\n')
    n = 100000
    d = 11
    print(f'Approximation of pi in {d} dimensons, when n = {n}:\t {sphere_volume(n,d)}')
    print(f'Exact value of pi in {d} dimensions:\t\t\t {hypersphere_exact(d)}')
    


if __name__ == '__main__':
	main()
