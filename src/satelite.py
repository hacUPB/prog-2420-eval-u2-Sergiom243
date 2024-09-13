def simular_desintegracion_orbital():
    
    altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en km): "))
    coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (por ejemplo, 0.01): "))
    altitud_minima_seguridad = float(input("Ingrese la altitud mínima de seguridad (en km): "))

   
    altitud_actual = altitud_inicial
    orbitas_completadas = 0
    perdida_altitud = 0

   
    while altitud_actual > altitud_minima_seguridad:
       
        perdida_altitud = coeficiente_arrastre * altitud_actual
        altitud_actual -= perdida_altitud
        orbitas_completadas += 1

        
        coeficiente_arrastre += 0.0000000001
        
        if perdida_altitud < 0.001:
            print(f"El satélite se ha estabilizado en una órbita baja.")
            print(f"Altitud final: {altitud_actual:.2f} km")
            print(f"Órbitas completadas: {orbitas_completadas}")
            return

   
    print(f"El satélite ha reingresado en la atmósfera terrestre y se ha desintegrado.")
    print(f"Número total de órbitas completadas: {orbitas_completadas}")


simular_desintegracion_orbital()
