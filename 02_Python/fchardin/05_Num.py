#importar un módulo
from math import *

n1 = 12
n2 = 22
n3 = 11.2
n4 = -9

n1s = str(n1)

print("ejemplos")
print(2 - 3)
print(n1 * n2)
print(3 - n1 * (n3 + n2))
print(10 % 3)
print(n1)

#transfomrando n1 a string podemos concatenarlo con otros strings
print(n1s + " ahora es un string :)" )

#funciones de números
#abs() devuelve el valor absoluto de un número (sin signo)
print("abs(x) devuelve el valor absoluto de x")
print(abs(n4))

#pow(x,y) (x: numero) elevado a la (y: potencia)
print("pow(x,y) devuelve la potencia de x elevado a y")
print(pow(n1, n2))

#max() y min() devuelven el máximo o el mínimo de un grupo de números
print("max")
print(max(n1, n2, n3, n4))
print("min")
print(min(n1, n2, n3, n4))
#round() redondea números flotantes a enteros
print("round(x) redondea x")
print(round(n3))

#floor() (piso) redondea para abajo y ceil() (techo) redondea para arriba
print(f"entrada " + str(n3))
print("floor(x) redondea x hacia abajo")
print(f"floor " + str(floor(n3)))
print("ceil(x) redondea x hacia arriba")
print(f"ceil " + str(ceil(n3)))
#sqrt (raíz cuadrada)
print("sqrt(x) devuelve la raíz cuadrada de x")
print(sqrt(n1))