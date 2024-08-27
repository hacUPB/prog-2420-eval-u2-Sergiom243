import random

from random import randint, uniform

#creo lista vacia
aleatorios = []
#se genera un n aleatorio
num_aleatorio = randint(10, 150)

#ingresar el numero a la lista
aleatorios.append(num_aleatorio)
print(aleatorios)
#para generar 100 n aleatorios

for i in range (100):
    num_aleatorio = randint(10, 150)
    aleatorios.append (num_aleatorio)

print(aleatorios)