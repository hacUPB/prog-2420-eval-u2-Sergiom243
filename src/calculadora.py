print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Módulo División")
opcion = int(input("ingrese la opción"))
operando1 = int(input("ingrese el primer valor"))
operando2 = int(input("ingrese el segundo valor"))

texto = ""

#si opcion = sumar
if  opcion <0 >5:
    resultado = ("no hay opciones")    

elif opcion == 1:
    resultado = operando1 + operando2
    texto = "+"
#si no, si oción = 2
elif opcion == 2:
    resultado = operando1 - operando2
    texto = "-"
elif opcion == 3:
    resultado = operando1 * operando2
    texto = "*"
elif opcion == 4:
    resultado = operando1 / operando2
    texto = "/"
elif opcion == 5:
    resultado = operando1 % operando2
    texto = "%"
else:
    print("opción no válida")

print(f"{operando1} {texto} {operando2}= {resultado}")