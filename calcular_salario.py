"""
Vas a capturar el nombre de una persona y el sueldo bruto que va a cobrar. Debes calcular el
sueldo neto de dicha persona. Se le descuenta como IRPF un 12% y en concepto de seguridad social
un 5'20%. Mostrar un mensaje "El sueldo neto de "nombre" es "tantos" euros

Modifica el ejercicio anterior para que el proceso se repita mientras el sueldo de la persona sea positivo.
Debes indicar el final del proceso, cuanto dinero recauda el estado en concepto de IRPF y cuanto en concepto
de Seguridad social, ademas de cuanto dinero invierte la empresa en total en la fuerza de trabajo.
Muestra una lista de sueldos netos con los nombres de los trabajadores

"""

# Capturamos el nombre de la persona


# def salarioNeto():
#     irpf = salario * 0.12
#     seguridadSocial = salario * 0.052
#     salarioNeto = salario - irpf - seguridadSocial
#     print(f"El sueldo neto de {nombre} es {salarioNeto} euros")
#
# salarioNeto()

seguridadSocialTotal = 0
irpfTotal = 0
listaTrabajadores = []

continuar = True
while continuar:
    nombre = input("Introduce tu nombre: ")
    salario = float(input("Introduce el salario: "))
    irpf = salario * 0.12
    seguridadSocial = salario * 0.052
    salarioNeto = salario - irpf - seguridadSocial
    seguridadSocialTotal += seguridadSocial
    irpfTotal += irpf
    if salario > 0:
        salarioNeto
        listaTrabajadores.append(f"{nombre}: {salarioNeto} euros")
        print(f"En total se recauda en irpf {irpfTotal} y en seguridad social {seguridadSocialTotal}")
        continuar = input("Deseas continuar? (si/no): ")
        if continuar == "no":
            continuar = False
            print(listaTrabajadores)
    else:
        print("el sueldo debe ser positivo")
        continuar = False
