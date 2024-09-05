#funcion que recibe: 1. Número de elementos. 2. rango de valores y retorna una lista. 
#la función recibe una lista de números de punto flotante y retorna su promedio.
#calcula cuántos elementos estan por encima del promedio de una lista y retorna ese valor.

from random import uniform #generea un número aleatorio flotante(uniform)

def creador_Lista(cantidad:int, lim_inf:float, lim_sup:float): #parámetros de la función, pueden ser especificos con el tipo de dato que se va a usar en la función
    #1. crear una lista vacía
    Lista = []
    #2. utilizar un bucle para generar los números y llenar la lista.
    for i in range(cantidad): #Range # de veces que se repite la cantidad
        #3 se genera un número aleatorio
        numero_aleat = uniform(lim_inf, lim_sup)
        #4. se agrega el número a la lista
        Lista.append(numero_aleat)
    return Lista

def calc_promedio(datos:list): #datos es una lista de números de punto flotante
    prom = sum(datos) / len(datos)
    return prom

def sobre_promedio(datos:list, promedio:float):
    cont = 0
    lista_mayores = []
    for i in datos:
        if i > promedio:
            cont += 1
            lista_mayores.append(i)
    return cont, lista_mayores


    


#programa principal
aleatorios = creador_Lista(100,0.0,10.0)
print(aleatorios)
promedio = calc_promedio(aleatorios)
print(f"el promedio es {promedio}")
cantidad, lista_mayores = sobre_promedio(aleatorios, promedio)
print (f"hay {cantidad} de valores por arriba del promedio y son estos números {lista_mayores}")