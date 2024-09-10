def simular_desintegracion_orbital():
    # Solicitar los datos de entrada al usuario
    altitud_inicial = float(input("Ingrese la altitud inicial del satélite (en km): "))
    coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (por ejemplo, 0.01): "))
    altitud_minima_seguridad = float(input("Ingrese la altitud mínima de seguridad (en km): "))

    # Variables iniciales
    altitud_actual = altitud_inicial
    orbitas_completadas = 0
    perdida_altitud = 0

    # Simulación de órbitas hasta que el satélite reingrese o se estabilice
    while altitud_actual > altitud_minima_seguridad:
        # Calcular la pérdida de altitud en esta órbita
        perdida_altitud = coeficiente_arrastre * altitud_actual
        altitud_actual -= perdida_altitud
        orbitas_completadas += 1

        # Aumentar el coeficiente de arrastre (simulando mayor resistencia a menor altitud)
        coeficiente_arrastre += 0.0001

        # Si la pérdida de altitud es muy pequeña, se considera que el satélite se estabiliza
        if perdida_altitud < 0.001:
            print(f"El satélite se ha estabilizado en una órbita baja.")
            print(f"Altitud final: {altitud_actual:.2f} km")
            print(f"Órbitas completadas: {orbitas_completadas}")
            return

    # Si el satélite reingresa en la atmósfera
    print(f"El satélite ha reingresado en la atmósfera terrestre y se ha desintegrado.")
    print(f"Número total de órbitas completadas: {orbitas_completadas}")

# Ejecutar la simulación
simular_desintegracion_orbital()
