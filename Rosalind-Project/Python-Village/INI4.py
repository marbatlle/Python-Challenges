# Conditions and Loops
rslt = 0
a = 4625
b = 9388
for i in list(range(a,(b+1))):
    if i%2 !=0:
        rslt += i
print(rslt)