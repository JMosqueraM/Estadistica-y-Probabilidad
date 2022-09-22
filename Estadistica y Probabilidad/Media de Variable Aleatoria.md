# Media de Variable Aleatoria ($\mu_x$)
Sea $X$ una variable aleatoria con distribucion de probabilidad $f(x)$. La media o valor esperado de $X$, si $X$ es discreta
![[Pasted image 20220914092323.png]]
Notese que:
- $x$ representa cada dato
- $f(x)$ representa la probabilidad de dicho dato

#### Ejercicio en clase 1
Un inspector de calidad obtiene una muestra de un lote que contiene 7 componentes; el lote contiene 4 componentes buenos y 3 defectuosos. El inspector toma una muestra de 3 componentes. Calcule el valor esperado del número de componentes buenos en esta muestra.

Es una distribucion de tipo **hipergeometrica**

Sea $X$ el numero de componentes buenos en la muestra. La distribucion de probabilidad de $X$ es
![[Pasted image 20220914092715.png]]
La primera combinacion

![[Pasted image 20220914093244.png]]
De esta manera, si de un lote de 4 componentes buenos y 3 defectuosos, se seleccionara al azar, una y otra vez, una muestra de tamaño 3, ésta contendría en promedio 1.7 componentes buenos.

#### Ejemplo en clase 2
Cierto día un vendedor de una empresa de aparatos médicos tiene dos citas. Considera que en la primera cita tiene 70 por ciento de probabilidades de cerrar una venta, por la cual podría obtener una comisión de $1000. Por otro lado, cree que en la segunda cita sólo tiene 40 por ciento de probabilidades de cerrar el trato, del cual obtendría $1500 de comisión. ¿Cuál es su comisión esperada con base en dichas probabilidades? Suponga que los resultados de las citas son independientes.

Se puede presentar 4 situaciones a partir de las dos citas.
- No cierra ni la primera ni la segunda cita $f(0)$ = $f(0)$ 
- No cierra la primera cita pero cierra la segunda $f(1)$ = $f(1500)$
- Cierra la primera cita pero no cierra la segunda $f(2)$ = $f(1000)$
- Cierra la primera y la segunda cita $f(3)$ = f(2500)

Tomando las probabilidades dadas, se puede crear el diagrama de arbol que nos va a permitir calcular las probabilidades de todos escenarios
![[Pasted image 20220914094922.png]]

![[Pasted image 20220914095004.png]]

Por lo tanto, la comision esperada del vendedor es:
![[Pasted image 20220914095356.png]]

#### Ejercicio en clase 3
![[Pasted image 20220914095437.png]]

Utilizando la definicion de **media** (o **valor esperado**), la vida esperada para el dispositivo se calcula planteando la siguiente integral
![[Pasted image 20220914095808.png]]

**RPTA:** Por lo tanto, esperamos que este tipo de dispositivo dure en promedio 200 horas.

# Media de una Variable Aleatoria (Que representa una densidad conjunta)
![[Pasted image 20220914101032.png]]

#### Ejercicio en clase 1
Calcule $E(Y|X)$ para la siguiente función de densidad
![[Pasted image 20220914101211.png]]

Primero se debe calcular la densidad marginal de de la variable aleatoria $Y$, es decir $h(y)$, por lo que se debe integrar la *funcion de densidad* con respecto a la variable $x$

![[Pasted image 20220914101621.png]]

# Otros Ejercicios
### Ejercicio 1
En el ejercicio 3.13 de la página 92 se presenta la siguiente distribución de probabilidad de $X$, el número de imperfecciones que hay en cada $10$ metros de una tela sintética, en rollos continuos de ancho uniforme
![[Pasted image 20220914101952.png]]

Calcule el numero promedio de imperfecciones que hay en cada 10 metros de esta tela. Esto se realiza mediante la ecuacion:
![[Pasted image 20220914102305.png]]

Que resulta en el siguiente calculo
$$= 0 \times f(0) + 1 \times f(1) + 2 f(2) + 3 \times f(3) + 4 \times f(4)$$

RPTA = El numero promedio de imperfecciones que hay en 10 metros de tela es en promedio 0.88

### Ejercicio 2
