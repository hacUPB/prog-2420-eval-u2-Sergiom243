#calculamos el promedio de edades
suma = 0
numero = int(input("ingrese el numero de estudiantes"))
cont = 1

while cont <= numero:
    edad = int(input("ingrese la edad"))
    suma = suma + edad
    cont = cont + 1

promedio = suma / numero
print(f"promedio de edades = {promedio}")