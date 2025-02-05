"""
Maquina de bebidas:
Agua = 0.50€
Refresco = 0.75€
Zumo = 0.95€

el programa emitira un menu que mostrara prodcutos y precios, ademas de la opcion salir.
Pedira la opcion elegida y pedira monedas al usuario

La maquina acepta todas las monedas de euro de 2€ a 5cts.

Al comienzo del dia la maquina dispone de 20 monedas de todas las cantidades necesarios
para el cambio.

Se debe dar el cambio correcto, con el menor numero posible de monedas.
La maquina mostrara un mensaje de "Introduzca importe exacto" en caso de no tener dos tipos
de moneda cualquiera o si una de los ausentes es la pila de 5cts. Solo aceptara el importe exacto en este caso.

Al final del programa nos debe dar el total del dinero disponible en la maquina, por unidad monetario.
"""

bebidas = ["Agua", "Refresco", "Zumo"]
precio = [0.50, 0.75, 0.95]
# valoresMonedas = [2, 1, 0.50, 0.20, 0.10, 0.05]
# reservaMonedas = [20, 20, 20, 20, 20, 20]
monedas = [[2, 20], [1, 20], [0.50, 20], [0.20, 20], [0.10, 20], [0.05, 20]]

def productos():
    print("Productos actuales de la maquina expendedora:\n")
    for productos, precios in zip(bebidas, precio):
        print(productos, precios)

def menu():
    print("1. Ver el menu")
    print("2. Elige una opcion")
    print("3. Salir")


def calcularCambio(montoIngresado, eleccion):
    cambio = montoIngresado - precio[eleccion]
    faltante = precio[eleccion] - montoIngresado
    if 0 < montoIngresado <= 2:
        if cambio < 0:
            print(f"Introduzca importe exacto, te faltante {faltante}")
        elif cambio == 0:
            print("Cambio exacto")
        else:
            print(f"El cambio a dar es: {cambio}")
    else:
        print("La maquina no acepta un monto superior a 2")

seguir = True

while seguir:
    menu()
    opcion = int(input("Elige una opcion: \n"))
    if opcion == 1:
        productos()
    if opcion == 2:
        productos()
        eleccion = int(input("Elige una bebida (1-3): ")) - 1
        if 0 <= eleccion < len(bebidas):
            montoIngresado = float(input("Ingresa el monto: "))
            calcularCambio(montoIngresado, eleccion)
        else:
            print("La opcion elegida no es valida")
    if opcion == 3:
        print("Has salido del programa")
        seguir = False


