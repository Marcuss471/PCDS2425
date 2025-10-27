"""
Solutions to module 1
Student: Marcus Steiner
Mail: marcus.steiner.3581@student.uu.se
Reviewed by: Andrey Shternshis
Reviewed date: 16/9 - 2024
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!
"""



import time
import math

def multiply(m: int, n: int) -> int:
    if m == 0 or n == 0:            #If either one is zero
        return 0                    #Return 0
    else:                           #Else
        return n + multiply(m-1, n) #itterate
    """ Computes m*n using additions"""


def harmonic(n: int) -> float:
    if n == 0:
        return "ERROR"
    elif n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)
    
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""


def get_binary(x: int) -> str:
    if x < 0:       #If negative
        return "-" + get_binary(-x)
    if x == 0:      #If zero
        return str(x)
    elif x == 1:    #If one
        return str(x)
    else:           #Reitterate
        return get_binary(x//2) + str(x%2)


def reverse_string(s: str) -> str:
    if len(s) <= 1: #If it's at the end
        return s
    else:           #Reitterate until end of string
        return s[-1] + reverse_string(s[:-1])
    """ Returns the s reversed """                  


def largest(a: iter):
    if len(a) <= 1:         #If the list has one element
        return a[0]                 #Return the largest element
    elif a[0] > a[-1]:      #If the firs element is larger than the last
        return largest(a[:-1])      #Return the list without the last element
    elif a[-1] >= a[0]:     #If the last element is larger or equal to the first element
        return largest(a[1:])       #Return the list witout the first element
    """ Returns the largest element in a"""


def count(x, s: list) -> int:
    if len(s) == 0:             #If the list is empty
        return 0
    
    elif x == s[0]:     #If its x
        return 1 + count(x, s[1:])  #Return 1 and recur the list without the first element
    
    elif type(s[0]) == list:      #Checks if next element is a list
        if len(s) >= 2:         #If there's more to the list
            return count(x, s[0]) + count(x, s[1:]) #Recursion in the next list and keeps going on the same list
        return count(x, s[0])   #If it isnt longer than one it just goes in on the new one
    
    else:
        return count(x, s[1:])      #Recur the list without the first element
    
    """
    if x == s[0]:
        return 1 + count(x, s[1:])
    if len(s) == 1:
        return 0
    else:
        return count(x, s[1:])
    """
    """ Counts the number of occurences of x on all levels in s"""
    


def bricklek(f: str, t: str, h: str, n: int) -> str:
    if n == 0:
        return []
    else:
        return bricklek(f, h, t, n-1) + [f'{f}->{t}'] + bricklek(h, t, f, n-1)
    """ Returns a string of instruction ow to move the tiles """


def fib(n: int) -> int:                      
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_mem(n: int, memory = None):
    if memory is None:
        memory = {0: 0, 1: 1}
    if n not in memory:
        memory[n] = fib_mem(n-1, memory) + fib_mem(n-2, memory)
    return memory[n]

def main():
    #print(multiply(5,7),"\n")
    
    #print(harmonic(2),"\n")
    
    #print(get_binary(-18),"\n")
    
    #print(reverse_string("Marcus"))
    
    #print(largest([13,6,89,89,2]))
    
    #print(count(4, [1, 4, 2, ['a', [[4], 3, 4]]]))
    
    #print(bricklek("f", "t", "h", 2))
    
    "EXCERCISE 9 & 10"
    
    x = 30
    
    if False:
        list_of_times = []
        for i in range(0,4):
            tstart = time.perf_counter()
            fib(x+i)
            tstop = time.perf_counter()
            print(f"Measured time for {x+i}: {tstop-tstart} seconds")
            list_of_times.append(tstop-tstart)
        
        time_increase = [(list_of_times[i]/list_of_times[i-1]) for i in range(1,len(list_of_times))]
        
        tot_time_increase = 0
        for i in range(0,len(time_increase)):
            tot_time_increase += time_increase[i]
            
        print(f'The avarage time increase: {tot_time_increase/len(time_increase)}')
    
    if False:
        tstart = time.perf_counter()
        print(f'The value of {x} in fibonacci is: {fib_mem(x)}')
        tstop = time.perf_counter()
        print(f"Measured time: {tstop-tstart} seconds")
    

if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
  
  If we input the formula that was found before with t(n) = 2^n - 1 we can input the number of tiles in n. So we get t(50) = 2^50 - 1 = 1 125 899 906 842 623
  It will take 35 702 052 years
  ~35,7 million years
  
  
  
  
  
  Exercise 9: Time for Fibonacci:
  
  a)
    The avarage time increase: 1.6097571103947275
    It's close to the estimated time of 1,618^n
  
  b)
    (s = seconds; c = constant; n = number of elements)
    s = c * theta(1,618^n)
    
    Let's input and try on n = 30 to get the constant c
    
    0,74716 = c * 1,618^30
    c = 0,74716/(1,618^30) = 4,018445616e-7 = 4,02 * 10^-7
    
    if n = 50
        s = 4,02 * 10^-7 * 1,618^50 = 11297,5 seconds
        or 3,14 hours

    if n = 100
        s = 4,02 * 10^-7 * 1,618^100 = 3,1762 * 10^14 seconds
        or 10,07 million years
  
  
  
  
  
  Exercise 10: Time for fib_mem:
  
  The value of 100 in fibonacci is: 354224848179261915075
  Measured time: 0.00033140000596176833 seconds
  or 0,3314 miliseconds
  
  
  
  
  
  Exercise 11: Comparison sorting methods:
  
  Start point: 10^3 elements in 1 second
  (s = seconds; c = constant; n = number of elements)
  s = c * theta(n)
  
  
  Insertion sort
    theta(n^2)
    Insert start point:
        1 = c * 10^3^2 = c * 10^6
        c = 1/10^6
        
    n = 10^6
        s = 1/10^6 * 10^6^2 = 10^12/10^6 = 10^6 seconds
        or 11,57 days
  
    n = 10^9
        s = 1/10^6 * 10^9^2 = 10^18/10^6 = 10^12 seconds
        or 31,7 thousand years
  
  
  Merge sort
    theta(n*log(n))
    Insert start point:
        1 = c * 10^3 * log(10^3)
        c = 1/(10^3 * 3) = 1/3000
        
    n = 10^6
        s = 1/3000 * 10^6 * log(10^6) = (10^6 * 6)/3000 = 2000 seconds
        or 33,33... min
        
    n = 10^9
        s = 1/3000 * 10^9 * log(10^9) = (10^9 * 9)/3000 = 3 000 000 seconds
        or 34,72 days

  
   
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
  A(n) = n
  B(n) = c * n * log(n)
  B(10) = 1 = c*10*log(10) = c*10*1
  c = 1/10
  
  A(n) = n
  B(n) = n*log(n)/10
  
  n = n*log(n)/10
  10 = log(n)
  n = 10^10
  When n = 10^10 algorithm A and B are at the same speed
  When n > 10^10 algorithm A is faster than algorithm B
  
"""