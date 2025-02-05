# str("string")
# int()
# float()
# variable = 3
# otraVariable = "saludos"
# num = int(input("Introduce un numero"))
# print(len(otraVariable))
# boolean = True o False
#
# lista = [1, 2, 3]

# 2 == 2
# 2 != 2
# 2 < 2
# 2 == 2 and 1 == 3
# not (2 != 2 or 1 == 1)
# if "a" in "aeiou" :
#     print("Hay a")

# esCierto = False
# while not esCierto:
#     print("aaa")
#     esCierto = True

# def tieneA(nombre):
#     if "a" in nombre.lower():
#         return True
#     return False
#
# lista = ["adrian", "antonio", "emily", "javier"]
# for i in range( len(lista)-1, -1, -1):
#     print(lista[i])
#
# for alumno in lista:
#     if tieneA(alumno):
#         print(f"{alumno.capitalize()} contiene la letra a")
bebidas = ["Agua", "Refresco", "Zumo"]
precio = [0.50, 0.75, 0.95]
monedas = [[2, 20], [1, 20], [0.50, 20], [0.20, 20], [0.10, 20], [0.05, 20]]  # [valor, cantidad]


def productos():
    print("\nProductos actuales de la máquina expendedora:\n")
    for i, (producto, precios) in enumerate(zip(bebidas, precio)):
        print(f"{i + 1}. {producto} - {precios:.2f}€")


def menu():
    print("\n1. Ver el menú")
    print("2. Elegir una bebida")
    print("3. Salir")


def darCambio(cambio):
    cambio_entregado = []

    for i in range(len(monedas)):
        valor, cantidad = monedas[i]
        while cambio >= valor and cantidad > 0:
            cambio -= valor
            cambio = round(cambio, 2)  # Evita errores de precisión con flotantes
            monedas[i][1] -= 1
            cambio_entregado.append(valor)

        if cambio == 0:
            break

    if cambio > 0:  # Si no se pudo dar el cambio exacto
        print("La máquina no puede dar cambio exacto. Introduzca importe exacto.")
        return False

    print("Cambio entregado:", cambio_entregado)
    return True


def calcularCambio(montoIngresado, eleccion):
    precio_bebida = precio[eleccion]
    cambio = montoIngresado - precio_bebida

    if montoIngresado < 0.05 or montoIngresado > 2:
        print("La máquina solo acepta monedas de 2€ a 5 céntimos.")
    elif cambio < 0:
        print(f"Introduzca importe exacto, faltan {abs(cambio):.2f}€")
    elif cambio == 0:
        print("Pago exacto. Compra realizada.")
        exit()
    else:
        if darCambio(cambio):
            print("Compra realizada.")
            exit()


seguir = True

while seguir:
    menu()
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        continue

    if opcion == 1:
        productos()
    elif opcion == 2:
        productos()
        try:
            eleccion = int(input("Elige una bebida (1-3): ")) - 1
        except ValueError:
            print("Entrada no válida. Introduce un número entre 1 y 3.")
            continue

        if 0 <= eleccion < len(bebidas):
            try:
                montoIngresado = float(input("Ingresa el monto: "))
                calcularCambio(montoIngresado, eleccion)
            except ValueError:
                print("Entrada no válida. Introduce un número válido.")
        else:
            print("La opción elegida no es válida.")
    elif opcion == 3:
        print("Has salido del programa.")
        seguir = False
    else:
        print("Opción no válida. Intente de nuevo.")

# Muestra el total de monedas disponibles al finalizar
print("\nTotal de dinero disponible en la máquina:")
for valor, cantidad in monedas:
    print(f"{valor:.2f}€: {cantidad} monedas")
