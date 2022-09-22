### Ejercicio 1
![[Pasted image 20220803091908.png]]
##### Solucion en codigo
```
hombre = [0.020, 0.002, 0.160, 0.102, 0.046, 0.084]
mujer = [0.024, 0.180, 0.018, 0.073, 0.088, 0.003]

ropaInt = (hombre[0], mujer[0])
camison = (hombre[1], mujer[1])
nada = (hombre[2], mujer[2])
pijama = (hombre[3], mujer[3])
camiseta = (hombre[4], mujer[4])
otros = (hombre[5], mujer[5])

# A: Ser Mujer
# B: Dormir desnuda
# P(A intersec B) = 0.018
print(nada[1] * 100)

# Probabilidad de un hombre viajero
print(sum(hombre) * 100)

# C: Sea Hombre
# D: Duerma con pillama
# P(D|C) = P(D intersec C) / P(C)
print(pijama[0] / sum(hombre) * 100)

# Probabilidad de que un viajero sea hombre si duerme con pijama o con camiseta
# P(C|EuD) = P(C|E) + P(C|D)
# ESTE PUNTO ESTA MAL
print((camiseta[0] / sum(hombre) + pijama[0] / sum(hombre)))

```

### Ejercicio 2
![[Pasted image 20220803095236.png]]


### Ejercicio 3
![[Pasted image 20220803095314.png]]

### Ejercicio 4
![[Pasted image 20220803103218.png]]

 P(D)