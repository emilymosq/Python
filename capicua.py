# Realiza un programa que pida un numero entero positivo de n cifras, y que compruebe
# si el número es capicua
# 12344321

def numCapicua():
    return input("Ingresa el número: ")

num = numCapicua()

numInvertido = num[::-1]

if num == numInvertido:
    print("El número es capicua.")
else:
    if num != numInvertido:
        print("El número no es capicua.")


#Otra manera

numero = input ("Introduzca su numero")
esCapicua= True
for i in range(len(numero)//2):
    if numero[i] != numero[-1 -i]:
        esCapicua = False
if esCapicua:
    print("El numero es capicua")
else:
    print("El numero no es capicua")