import random as r

# La maquina crea un num aleatorio del 1 al 100, el jugador intenta adivinar hasta que lo consigue y la maquina da pistas.

num = r.randint(1, 100)

haAcertado = False
while not haAcertado:
    intento = int(input("introduce un num del 1 al 100"))
    if num > intento:
        print("El numero es mayor")
    elif num < intento:
        print("El numero es menor")
    else:
        print("Has acertado!")
        haAcertado = True


