edades = [23, 45, 34, 12, 33, 43, 76, 34, 56, 55, 76, 33, 43, 76, 34, 56, 55, 76 ]
#abarca todas las edades y ejecuta la edad en 10 años
for edad in edades:
    print(f"edad en 10 años: {edad+10}")

#bucle para todos los elementos de la lista por separado
indice = 0
numero = len(edades)
while indice < numero:
    print(f"edad en 10 años: {edades[indice] + 10}")
    indice += 1
#es un rango de numero que se desea y con saltos de cuanto entre cada numero
for i in range (numero):
    print(f"edad en 10 años: {edades[i]+ 10}")

    

