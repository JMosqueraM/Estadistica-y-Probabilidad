## Probabilidad
La probabilidad de la union de dos eventos es igual a la suma de la probabilidad de los eventos, menos la probabilidad de interseccion entre los dos eventos:
$$P(E_1 \cup E_2) = P(E_1) + P(E_2) - P(E_1 \cap E_2)$$
### Probabilidad Condicional
La probabilidad de que ocurra un evento dependiendo de si otro evento haya ocurrido o no.
$$P(A \mid B)= \frac{P(A \cap B)}{P(B)}$$
#### Ejemplo
![[Pasted image 20220801092046.png]]


---
Si $A$ y $B$ son independientes:
$$P(A \mid B)=P(A)$$
$$P(B \mid A)=P(B)$$

### Regla del Producto
$$P(A \cap B)= P(A \mid B)=P(A \mid B)\times P(B)$$
Donde: $P(B) > 0$

#### Ejemplo 1
Suponga que tenemos una caja de fusibles que contiene 20 unidades, de las cuales 4 es tan ddefectuosas. Si se seleccionan 2 fusibles al azar y se retiran de la caja, uno despues del otro, sin reemplazar el primero, ¿Cual es la probabilidad de que ambos fusibles esten defectuosos?
![[Pasted image 20220801094015.png]]

#### Ejemplo 2
Una bolsa contiene 4 bolas blancas y 3 negras, y una segunda bolsa contiene 3 blancas y 5 negras. Se saca una bola de la primera bolsa y se coloca sin verla en la segunda bolsa. ¿Cual es la probabilidad de que ahora se saque una bola negra de la segunda bolsa?

$N_1:$ "Sacar una bola negra de la primera bolsa"
$N_2:$ "Sacar una bola negra de la segunda bolsa"
$B_1:$ Sacar una bolda blanca de la primera bolsa"
$$ \, $$
$$P(N_1 \cap N_2) \, ó \, P(B_1 \cap N_2)$$
$$=P(N_1 \mid N_2) \times P(N_1) + P(N_2 \mid B_1) P(B_1)$$

$$= \frac{2}{3} \times \frac{3}{7} + \frac{5}{9} \times \frac{4}{7}$$
$$ \therefore \frac{38}{63}$$
