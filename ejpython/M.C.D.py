def calcular_divisores (numero:int): 
    Divisores = []
    for divisor in range (1, numero + 1):
        if numero % divisor == 0:
            Divisores.append(divisor)
    return Divisores

def maximo_comun_divisor(lista1:list, lista2:list):
    elem_l1 = len(lista1)
    for i  in range (elem_l1-1 , -1, -1):
        if lista2.count(lista1[i]) == 1:
            return lista1[i]
    return -1

def simplifica_fraccion(num1:int, num2:int, mcd:int):

    numerador = num1/mcd
    denominador = num2/mcd
    print (f'{num1}/{num2} = {numerador}/{denominador}')

Lista_num = calcular_divisores (469)
Lista_den = calcular_divisores (33)
print(f'divisores del numerador: {Lista_num}')
print (f'divisores del denominador: {Lista_den}')

mcd = maximo_comun_divisor (Lista_num, Lista_den)
print (f'el máximo comun divisor es {mcd}')