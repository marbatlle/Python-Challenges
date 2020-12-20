# Mortal Fibonacci Rabbits
## http://rosalind.info/problems/fibd/



"""
for n,m
return the total number of pairs of rabbits that will remain after the
n-th month if all rabbits live for m months
"""

from typing import overload


def Fibonacci_Loop_Pythonic(months):
    parent,child = 1,1
    for itr in range(months-1):
        child = parent 
        parent = parent + (child*offspring)
    return new  

print(Fibonacci_Loop_Pythonic(12 ))

def Fibonacci_Loop_Pythonic(months,life):
    parent,child = 1,1
    for itr in range(months-1):
        child = parent 
        parent = parent + (child*1)
    return new  
