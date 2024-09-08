import random
precio = 0
Distancia = 0
Ciudades = ["Medellín","Cartagena", "Bogotá" ]
Asientos = ["Ventana", "Pasillo","Medio","Aleatorio"]
Dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

opciones = ["Sr", "Sra"]

identificación = input(f"por favor ingrese si se identifica como ({opciones [0]} o {opciones [1]})")

while True:
    if identificación in opciones:
        nombre = input (f"por favor introduce tu nombre completo")
        print(f"{identificación} {nombre} Bienvenid@ a FastFast Airlines ")
        break
    else:
        print(f"por favor elige una opcion valida entre ({opciones [0]} o {opciones [1]})")
        break

        input (f"Elige una ciudad de origen ({Ciudades [0]}, {Ciudades [1]} ó {Ciudades [2]}")

    

    
    


     
        

