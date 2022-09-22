###### Indice
- [[#Distribuciones de Probabilidad Conjunta]]
	- [[#Para Variables Aleatorias Discretas]]
	- [[#Ejemplo General]]
	- [[#Ejemplo Densidad Conjunta Discreta]]
	- [[#Para Variables Aleatorias Continuas]]
	- [[#Ejemplo Particular Densidad Conjunta Continua]]
- [[#Distribuiciones Marginales]]
	- [[#Ejemplo]]
	- [[#Distribucion de Probabilidad Condicional]]
		- [[#Para Variables Aleatorias Discretas]]
		- [[#Para Variables Aleatorias Continuas]]
- [[#Links]]

###### Resumen General
![[Pasted image 20220911174630.png]]

# Distribuciones de Probabilidad Conjunta
Es una funcion que calcula la [[Probabilidad]] de ocurrencia de **dos** o mas variables aleatorias[^2] **al mismo tiempo**

Se utiliza en situaciones en las que se busque registrar los resultados simultaneos de diversas variables aleatorias.

Por ejemplo, en un experimento quimico controlado podriamos medir la cantidad del precipitado $P$ y la del volumen $V$ de gas liberado, lo que daria lugar a un espacio muestral bidimensional que consta de los resultados $(p, v)$.

### Para Variables Aleatorias Discretas
Si X y Y son dos variables aleatorias **discretas**, la distribución de probabilidad para sus ocurrencias simultáneas se representa mediante una función con valores $f (x, y)$, para cualquier par de valores $(x, y)$ dentro del rango de las variables aleatorias $X$ y $Y$. Y la **distribcuion de probabilidad conjunta** se denota como:
$$f (x, y) = P (X = x, Y = y)$$
> Es decir, los valores f (x, y) dan la probabilidad de que los resultados $x$ y $y$ ocurran **al mismo tiempo**.


La funcion $f(x, y)$ es una **distribucion de probabilidad conjunta** o **funcion de masa de probabilidad**[^3]  de las variables aleatorias discretas[^1] $X$ y $Y$, si se cumple:
![[Pasted image 20220911101929.png]]

###### Ejemplo General
Si se le va a dar servicio a los neumáticos de un camión de transporte pesado, y $X$ representa el número de millas que éstos han recorrido y $Y$ el número de neumáticos que deben ser reemplazados, entonces $f (30,000, 5)$ es la probabilidad de que los neumáticos hayan recorrido más de 30,000 millas y que el camión necesite 5 neumáticos nuevos.

##### Ejemplo Densidad Conjunta Discreta
![[Pasted image 20220911132354.png]]
![[Ejem-1.png]]
![[Pasted image 20220911132640.png]]

### Para Variables Aleatorias Continuas
Cuando $X$ y $Y$ son variables aleatorias continuas, la función de densidad conjunta $f (x,y)$ es una superfi cie que yace sobre el plano $xy$, y $P[(X,Y) ∈ A]$, donde A es cualquier región en el plano xy, que es igual al volumen del cilindro recto limitado por la base $A$ y la superfi cie.

La funcion $f(x, y)$ es una **función de densidad conjunta** de las variables aleatorias continuas $X$ y $Y$ si

![[Pasted image 20220911154642.png]]

##### Ejemplo Particular Densidad Conjunta Continua
Una empresa privada un local que da servicio a clientes que llegan en automovil y otro que da servicio a clientes que llegan caminando. En un dia elegido al azar, sean $X$ y $Y$, respectivamente, las proporciones de tiempo que ambos locales estan en servicio, y suponiendo que la funcion de densidad conjunta de estas variables aleatorias es:
![[Pasted image 20220911154731.png]]1. Verifique la condicion 2 de la definicion 3.9
La condicion a cumplir es:
![[Pasted image 20220911154751.png]]
Para encontrarlo se efectua la doble derivada de la funcion de densidad teniendo como limites las restricciones de $x$ y $y$ en la funcion de densidad conjunta. 
![[Pasted image 20220907093738.png]]
$$\frac{2}{5} [y+\frac{3y^2}{2}] |_0^1 = 1$$
2. Calcule $P[(x, y)] \in A]$, donde $A = \{ (x, y) | 0 < x < \frac{1}{2}, \frac{1}{4} < y < \frac{1}{2} \}$

![[Pasted image 20220911161952.png]]

## Distribuiciones Marginales
Dada la distribución de probabilidad conjunta $f (x, y)$ de las variables aleatorias discretas $X$ y $Y$, la distribución de probabilidad $g(x)$ sólo de $X$ se obtiene sumando $f (x, y)$ sobre los valores de $Y$. De manera similar, la distribución de probabilidad $h(y)$ de sólo Y se obtiene sumando $f (x, y)$ sobre los valores de $X$. 

Definimos $g(x)$ y $h(y)$ como **distribuciones marginales de** $X$ y $Y$, respectivamente. Cuando $X$ y $Y$ son *variables aleatorias continuas*, las **sumatorias** se reemplazan por **integrales**.

Ahora podemos establecer la siguiente definición general.
![[Pasted image 20220911163137.png]]

#### Ejemplo Distribuciones Marginales
![[Pasted image 20220911163943.png]]

## Distribucion de Probabilidad Condicional
Es la funcion de proabilidad de una variable aleatoria dada la ocurrencia de la otra variable de una funcion $f(x, y)$
![[Pasted image 20220911164045.png]]

#### Para Variables Aleatorias Discretas
Si deseamos encontrar la probabilidad de que la variable aleatoria Si deseamos encontrar la probabilidad de que la variable aleatoria discreta $X$ caiga entre $a$ y $b$ cuando sabemos que la variable discreta $Y = y$, evaluamos $X$ caiga entre $a$ y $b$ cuando sabemos que la variable discreta $Y = y$, evaluamos
![[Pasted image 20220911164348.png]]

donde la sumatoria se extiende a todos los valores de $X$ entre $a$ y $b$

#### Para Variables Aleatorias Continuas
Si deseamos encontrar la probabilidad de que la variable aleatoria **continua** $X$ caiga entre $a$ y $b$ cuando sabemos que la variable continua $Y = y$, evaluamos
![[Pasted image 20220911164340.png]]


###### Links
[^1]: [[Variable Aleatoria Discreta]]
[^2]: [[Variable Aleatoria]]
[^3]: [[Funcion de Probabilidad]]
