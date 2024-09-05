from os import system

while True: #Bucle infinito
    print("1. Calcular primo\n 2. calcular par\n 3. Salir")
    opcion = int(input("ingrese la opcion"))

    if opcion == 1:
        system ("cls")
        num = int(input("ingrese un número"))
        cont = 0
        control = 1
        while control <= num:
            if (num % control) == 0:
                cont += 1
            control += 1

        if cont > 2:
            print(f"{num} No es primo")
        else:
            print(f"{num} Es primo")
    elif opcion == 2:
        system ("cls")
        num = int(input("ingrese un número"))
        if num % 2 ==0:
            print (f"{num} es par")
    elif opcion == 3:
        system ("cls")
        break  #Rompe el bucle infinito
    else:
        print("opcion no válida.")
