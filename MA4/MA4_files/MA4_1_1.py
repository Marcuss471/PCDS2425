
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import random as r
import matplotlib.pyplot as plt 
import math     #To print the constant for pi

def approximate_pi(n):
    coordinates = {
        'X':[r.uniform(-1,1) for x in range(n)] ,
        'Y':[r.uniform(-1,1) for x in range(n)] ,
        'X_circle':[] , 
        'Y_circle':[] ,
        'X_outside':[] ,
        'Y_outside':[]
    }
    
    for index in range(len(coordinates['X'])):
        if (coordinates['X'][index]**2 + coordinates['Y'][index]**2) <= 1:
            coordinates['X_circle'].append(coordinates['X'][index])
            coordinates['Y_circle'].append(coordinates['Y'][index])
        else:
            coordinates['X_outside'].append(coordinates['X'][index])
            coordinates['Y_outside'].append(coordinates['Y'][index])
        
    plt.scatter(coordinates['X_outside'], coordinates['Y_outside'], color='blue')
    plt.scatter(coordinates['X_circle'], coordinates['Y_circle'], color='red')
    
    plt.show()
    
    return (4*len(coordinates['X_circle'])/n)
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        print(f'approximation of pi: {approximate_pi(n)}')
    print(f'builtin constant pi: {math.pi}')
    
if __name__ == '__main__':
	main()