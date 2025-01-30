"""
Mostras el sig menu para que el usuario decida:
1. Calcular si el numero que le pasas es primo -> %0 1 y N
2. Calcular si el numero que le pasas es par -> N % N -> resto
3. Calcular si el numero que le pasas es bisiesto ->
        Divisible por 4. No divisible por 100.
        Salvo si es divisible por 400.
        (2000 y 2400 son bisiestos pues aún siendo divisibles por 100 lo son también por 400.
        Pero los años 1800, 1900, 2100, 2200 y 2300 no lo son porque solo son divisibles por 100).
"""
def menu():
    print("1. Calcular si el numero es primo: ")
    print("2. Calcular si el numero es par: ")
    print("3. Calcular si el numero es bisiesto: ")
    print("4. Salir")

def esPar():
    return numero % 2 == 0

def esPrimo():
    if numero < 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def esBisiesto():
    if numero % 400 == 0:
        return True
    if numero % 4 == 0 and numero % 100 != 0:
        return False
    return False


seguir = True

while seguir:
    menu()
    opcion = int(input("Elige una opcion: "))
    if opcion != 4:
        numero = int(input("Introduce un numero:"))
    if opcion == 1:
            if esPrimo():
                print(f"El numero {numero} es primo")
            else:
                print(f"El numero {numero} no es primo")
    if opcion == 2:
            if esPar():
                print(f"El numero {numero} es par")
            else:
                print(f"{numero} no es par")
    if opcion == 3:
        if esBisiesto():
            print(f"El año {numero} es bisiesto")
        else:
            print(f"El año {numero} no es bisiesto")
    if opcion == 4:
        print("Has salido del programa")
        seguir = False


