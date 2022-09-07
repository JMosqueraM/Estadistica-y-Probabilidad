# Chi Cuadrado
Se utiliza para determinar si los datos de una muestra se ajustan para representar una poblacion. Por otro lado, tambien es usado para comprobar o rechazar hipotesis. El puntaje se denota: $$X_c^2$$
En donde:
- $X^2:$ Quiere decir "Chi Cuadrado"
- $c:$ Grados de linertad

#### Calcular Chi Cuadrado
La prueba estadistica de chi cuadrado se rige por la formula:
![[Pasted image 20220907080025.png]]
o tambi:
![[Pasted image 20220907080102.png]]
En donde:
- $O_i :$ Valor observado
- $E_i:$ Valor esperado
Y por ende:
$$Residual = O_i - E_i$$
$$Componente = \, \frac{Residual^2}{E_i}$$
El "puntaje" de la prueba chi cuadrado se obtiene commo la sumatoria de todas las $componentes$ calculadas
$$\sum_{i = 0}^{\# \, Componentes} Componente_i$$

#### Calcular grados de libertad ($c$)
Si no se dan los grados de libertad en un problema, estos se puede calcular:
$$ Grados \, de \, libertad\, = \, \#
\,de\, categorias$$


#### Probar Hipotesis con Chi Cuadrado (prueba de independencia)
Para realizar la prueba debes tener:
- Los *grados de libertad* (ver [[#Calcular grados de libertad c]]
- La estadistica "puntaje" chi cuadrado (ver [[#Calcular Chi Cuadrado]])
- Tabla de Chi Cuadrado (ver [[Tabla Chi Cuadrado]])

Pasos:
1) Ubicar en la [[Tabla Chi Cuadrado]], *primera columna* los **grados de libertad**.
2) En la fila correspondiente a los **grados de libertad**, ubicar:
	1) El valor exacto de del **estadistica chi cuadrado**
	2) En caso de que no se encuentre el *valor exacto*, buscar el **par de valores** que definan el *rango* en donde se ubica la **estadistica chi cuadrado**
3) Ubicar el valor decimal (area) $\longrightarrow\, Valor\, p$:
	1) En caso de `2.1` ubicar el valor que se situa sobre la columna donde se encontro el valor.
	2) En caso de `2.2` calcular el promedio entre los valores que se situan sobre las columnas del **par de valores** que definen el *rango*.

A partir del *valor p* calculado se acepta o rechaza la hipotesis:
- A menor valor del puntaje p es mas aceptable **rechazar** la hipotesis evaluada.
- A mayor valor del puntaje p es mas aceptable **aceptar** la hipotesis evaluada.