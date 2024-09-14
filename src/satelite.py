orbita = 0

Altitud_inicial = float(input("por favor ingrese una altitud inicial en km: "))
Altitud_mínima = float(input("por favor ingrese una altitud de seguridad en km: "))
Coeficiente_arrastre = float(input("por favor ingrese un coeficiente de arrastre(ejemplo: 0.01): "))

final_simulacion = True 
while final_simulacion:

    cambio_altitud = Altitud_inicial * Coeficiente_arrastre
    Diferencia_altitud = Altitud_inicial - cambio_altitud
    orbita += 1
    Coeficiente_arrastre += 0.0001 

    if Diferencia_altitud < Altitud_mínima:
        print (f"el satelite regreso a la órbita y se desintegró, logro {orbita} orbitas")
        final_simulacion = False

    if Diferencia_altitud < :
        print (f"el satelite se estabilizó a las {orbita} orbitas")
        final_simulacion = False



    print (f"Orbita: {orbita} altitud en km: {Diferencia_altitud} y coeficiente de arrastre: {Coeficiente_arrastre}")
