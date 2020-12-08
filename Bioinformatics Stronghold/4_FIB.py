# Rabbits and Recurrence Relations
## http://rosalind.info/problems/fib/

n = 5
k = 3
parent = 1
child = 1

while n >= 1:
    pairs = pairs*k
    n -= 1

print(pairs)

"""
o - small (children) rabbits. They have to mature and reproduce in the next cycle only.
0 - mature (parents) rabbits. They can reproduce and move to the next cycle.

Month 1: [o]
Month 2: [0]
Month 3: [0 o o]
Month 4: [0 o o 0 0]
Month 5: [0 o o 0 0 0 o o 0 o o]
Month 6: [0 o o 0 0 0 o o 0 o o 0 o o 0 0 0 o o 0 0]
"""
