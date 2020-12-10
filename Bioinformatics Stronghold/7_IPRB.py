# Mendel's First Law
## http://rosalind.info/problems/iprb/
import itertools

k = 25 # num homozygous dominant individuals
m = 16 # num heterosygous individuals
n = 23 # num homozygous recessive individuals

pop = [*(['d']*k), *(['h']*m), *(['r']*n)] # population

# propability that a pair produces dominant allele ind.
n = 0
p = 0
d = {('d','d'): 1, ('d','h'): 1, ('d','r'): 1,
     ('h','h'): 3/4, ('h','r'): 1/2, ('r','r'): 0}

for i,j in itertools.combinations(pop, 2):
    n += 1
    p += d[(i,j)]

result = p/n
print(result)