import math

from numpy import append

# Syntax: math.comb(n, k)
# Syntax: math.perm(n, k)

# Parameters:
# n: A non-negative integer
# k: A non-negative integer

lista = []
for i in range(6):
    for j in range(6):
        item = i + j
        lista.append(item)
print(lista)