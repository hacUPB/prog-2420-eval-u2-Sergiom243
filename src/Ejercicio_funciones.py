Lista = [4, 5, 7, 34, 54, 65, 76, 3, 4, 54, 34, 23, 22, 11] 

acum = 0 
cont = 0
num_elemen = len(Lista)

while cont < num_elemen:
    acum += Lista[cont]
    cont += 1

sumatoria = sum(Lista)

print(f"si el el código es correcto{acum}= {sumatoria}")

acum = 0

for elemento in Lista:
    acum += elemento

print(f"usando el bucle, la suma es {acum}")

#ejemplo de sort. Ordena de menor a mayor la lista. en el parentesis del sort se puede usar reverse=True para lista de mayor a menor

print(Lista)
Lista.sort()
print(Lista)

