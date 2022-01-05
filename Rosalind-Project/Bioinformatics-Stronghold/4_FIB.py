# Rabbits and Recurrence Relations
## http://rosalind.info/problems/fib/

"""
r1 - First Generation
r2 - Second Generation
k -  every pair of reproduction-age rabbits produces a litter of k rabbit pairs 
n - total number of months / cycles
"""


def rabbit(n,k):
    r1 = 1
    r2 = 1
    if n == 0:
        return r1
    elif n == 1:
        return r2
    else:
        for i in range(2,n):
            rn = r1 * k + r2
            r1 = r2
            r2 = rn
        return r2

print(rabbit(28,4))