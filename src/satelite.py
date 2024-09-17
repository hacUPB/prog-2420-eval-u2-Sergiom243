orbita = 0
incremento_arrastre = 0

verificacion_altitud = True
while verificacion_altitud:
    Altitud_inicial = float(input("Por favor ingrese una altitud inicial en km: "))
    Altitud_mínima = float(input("Por favor ingrese una altitud de seguridad en km: "))

    if Altitud_inicial <= Altitud_mínima:
        print("Error: La altitud inicial debe ser mayor que la altitud mínima. Intente de nuevo.")
    else:
        verificacion_altitud = False 

Coeficiente_arrastre = float(input("Por favor ingrese un coeficiente de arrastre (ejemplo: 0.01): "))
incremento_arrastre += 0.00001   

final_simulacion = True
while final_simulacion:
    cambio_altitud = Altitud_inicial * Coeficiente_arrastre
    Diferencia_altitud = Altitud_inicial - cambio_altitud
    Altitud_inicial = Diferencia_altitud
    orbita += 1

    if Diferencia_altitud < Altitud_mínima:
        print(f"El satélite regresó a la atmósfera y se desintegró. Logró {orbita} órbitas.")
        final_simulacion = False

    elif cambio_altitud < 0.01:
        print(f"El satélite se estabilizó a las {orbita} órbitas.")
        final_simulacion = False

    else:
        print(f"Órbita: {orbita} - Altitud en km: {Diferencia_altitud:.2f} - Coeficiente de arrastre: {Coeficiente_arrastre:.4f}")