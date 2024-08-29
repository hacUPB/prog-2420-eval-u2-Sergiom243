#calculamos ahorro durante 1 año
suma = 0
n = 1
while n <= 365:
    valor = 3 ** n
    suma = suma + valor
    # tambien se puede usar suma += valor
    n += 1

pesos = suma / 100
print(f"el total ahorrado es de {pesos}")