"""
Vas a capturar el nombre de una persona y el sueldo bruto que va a cobrar. Debes calcular el
sueldo neto de dicha persona. Se le descuenta como IRPF un 12% y en concepto de seguridad social
un 5'20%. Mostrar un mensaje "El sueldo neto de "nombre" es "tantos" euros
"""

# Capturamos el nombre de la persona
nombre = input("Introduce tu nombre: ")
salario = int(input("Introduce el salario: "))

def salarioNeto():
    irpf = salario * 0.12
    seguridadSocial = salario * 0.052
    salarioNeto = salario - irpf - seguridadSocial
    print(f"El sueldo neto de {nombre} es {salarioNeto} euros")

salarioNeto()