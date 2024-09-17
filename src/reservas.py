import random
from os import system
from datetime import datetime

Distancia = 0
Ciudades = ["Medellín","Cartagena", "Bogotá" ]
Asientos = ["Ventana", "Pasillo","Medio","Aleatorio"]
Genero = ["Sr", "Sra"]

Fila = random.randint (1,29)

while True:
    gnr = input('por favor ingrese si se identifica como Sr o Sra: ')
    if gnr in Genero:
        break    
    print("Por favor, revisar la opción ingresada")

Nombre = input ('Por favor ingrese su nombre completo: ')
print (f'{gnr} {Nombre} Bienvenid@ a FastFast Airlines')

verificar_Destino = True
while verificar_Destino:
    Destino= str(input('Por favor ingrese la ciudad de Destino (Medellín: 1), (Cartagena: 2), ó (Bogotá: 3): '))
    if Destino == "1":
        verificar_Destino = False
        print("Destino es Medellín")
    elif Destino == "2":
        verificar_Destino = False
        print("Destino es Cartagena")
    elif Destino == "3":
        verificar_Destino = False
        print("Destino es Bogotá")
    else:
        print("Por favor digite el número de la ciudad correspondiente")

verificar_origen = True
while verificar_origen:
    Origen = str(input('Por favor ingrese la ciudad de origen (Medellín: 1), (Cartagena: 2), ó (Bogotá: 3): '))
    if Origen == Destino:
        print("la ciudad de origen no puede ser la misma del destino")
        continue
    if Origen == "1":
        verificar_origen = False
        print("Origen es Medellín")
    elif Origen == "2":
        verificar_origen = False
        print("Origen es Cartagena")
    elif Origen == "3":
        verificar_origen = False
        print("Origen es Bogotá")
    else:
        print("Por favor digite el número de la ciudad correspondiente")

while True:                 
    fecha_ingresada = input ("ingrese la fecha de su vuelo en este formato dd/mm/yyyy: ")
    try:
        fecha_usuario = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
        Dia_semana = fecha_usuario.isoweekday()
        if fecha_usuario >= datetime.now():
            break
        print ("la fecha ingresada es incorrecta")
    except ValueError:
        print ("el formato de la fecha es incorrecto") 

if (Origen == "3" and Destino == "1") or (Origen == "1" and Destino == "3"):
    Distancia = "1"
elif (Origen == "3" and Destino == "2") or (Origen == "2" and Destino == "3") or (Origen == "1" and Destino == "2") or (Origen == "2" and Destino == "1"):
    Distancia = "2"

if Distancia == "1" and Dia_semana <= 3:
    precio_final = 79900
elif Distancia == "1" and Dia_semana > 3:
    precio_final = 156000
elif Distancia == "2" and Dia_semana <= 3:
    precio_final = 119900
elif Distancia == "2" and Dia_semana > 3:
    precio_final = 213000

Revisar_Asientos = True
while Revisar_Asientos:
    Asiento = input("Por favor ingresar su asiento de preferencia (Ventana), (Pasillo), (Medio), (Aleatorio): ")
    if Asiento not in Asientos:
        print ("Por favor ingresar un lugar de asiento válido")
        continue

    if Asientos  == 'Ventana':
        Puesto_Asignado = "A"
        Revisar_Asientos = False
    elif Asientos == 'Pasillo':
        Puesto_Asignado = "B"
        Revisar_Asientos = False
    elif Asientos == 'Medio':
        Puesto_Asignado = "C"
        Revisar_Asientos = False
    else: 
        Puesto_Asignado = "F"
        Revisar_Asientos = False

print (f"Su reserva ha sido confirmada. \n El vuelo desde {Origen} hacia {Destino} ha sido confirmado con éxito, para {fecha_ingresada}\n Pasajero: {Nombre} Asiento: {Fila} {Puesto_Asignado} por un precio total de ${precio_final} ")


