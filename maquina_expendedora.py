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
valoresMonedas = [2, 1, 0.50, 0.20, 0.10, 0.05]
reservaMonedas = [20, 20, 20, 20, 20, 20]