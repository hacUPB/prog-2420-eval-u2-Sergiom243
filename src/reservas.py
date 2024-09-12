import random
from os import system
from datetime import datetime

Distancia = 0
Ciudades = ["Medellín","Cartagena", "Bogotá" ]
Asientos = ["Ventana", "Pasillo","Medio","Aleatorio"]
Dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
Genero = ["Sr", "Sra"]

Fila = random.randint (1,29)

while True:
    gnr = input('por favor ingrese si se identifica como Sr o Sra: ')
    if gnr in Genero:
        break    
    print("Por favor, revisar la opción ingresada")

Nombre = input ('Por favor ingrese su nombre completo: ')
print (f'{gnr} {Nombre} Bienvenid@ a FastFast Airlines')

while True:
    Destino = input('Ingrese su ciudad de destino (Medellín), (Cartagena) ó (Bogotá): ')
    if Destino in Ciudades:
        break
    print ('ingrese una opción valida')

while True:
    Origen = input ('Por favor ingrese la ciudad de origen (Medellín), (Cartagena), ó (Bogotá): ')
    if Origen in Ciudades and Origen != Destino:
        break
    print ("Por favor ingresar una ciudad de origen distinta a su destino")

while True:                 
    fecha_ingresada = input ("ingrese la fecha de su vuelo en este formato dd/mm/yyyy: ")
    try:
        fecha_usuario = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
        if fecha_usuario >= datetime.now():
            break
        print ("la fecha ingresada es incorrecta")
    except ValueError:
        print ("el formato de la fecha es incorrecto") 

while True:
    Dia = input("ingrese el día de la semana que va a viajar (Lunes), (Martes), (Miércoles), (Jueves), (Viernes), (Sábado), (Domingo): ")
    if Dia in Dias:
        break
    print ("Por favor elegir un dia de la semana existente")

if (Origen=="Bogotá" and Destino == "Medellín") or (Origen=="Medellín" and Destino == "Bogotá"):
    Distancia = 1
elif (Origen == "Bogotá" and Destino == "Cartagena") or (Origen == "Cartagena" and Destino == "Bogotá") or (Origen == "Medellín" and Destino == "Cartagena") or (Origen == "Cartagena" and Destino == "Medellín"):
    Distancia = 2

if Distancia == 1:
    if Dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
        precio_final = 79900
    elif dia in ["Sábado", "Domingo"]:
        precio_final = 156000
elif Distancia == 2:
    if Dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
        precio_final = 119900
    elif Dia in ["Sábado", "Domingo"]:
        precio_final = 213000

while True:
    Asiento = input("Por favor ingresar su asiento de preferencia (Ventana), (Pasillo), (Medio), (Aleatorio): ")
    if Asiento not in Asientos:
        print ("Por favor ingresar un lugar de asiento válido")
        continue

    if Asientos  == 'Ventana':
        Puesto_Asignado = "A"
    elif Asientos == 'Pasillo':
        Puesto_Asignado = "B"
    elif Asientos == 'Medio':
        Puesto_Asignado = "C"
    else: 
        Puesto_Asignado = "F"

print (f"Su reserva ha sido confirmada. \n El vuelo desde {Origen} hacia {Destino} ha sido confirmado con éxito, para el dia {Dia} {fecha_ingresada}\n Pasajero: {Nombre} Asiento: {Fila} {Puesto_Asignado} por un precio total de ${precio_final} ")


