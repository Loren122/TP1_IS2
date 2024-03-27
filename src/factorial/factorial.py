#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(desde, hasta): 
    # Itera sobre cada número en el rango desde 'desde' hasta 'hasta' inclusive
    for num in range(desde, hasta+1):
        # Si el número es negativo, imprime un mensaje de error
        if num < 0: 
            print("Factorial de un número negativo no existe")
        # Si el número es cero, imprime que el factorial de 0 es 1
        elif num == 0: 
            print("Factorial de 0 es 1")
        else: 
            fact = 1
            # Guarda el valor original de num en la variable n
            n = num  
            # Calcula el factorial del número
            while(num > 1): 
                fact *= num 
                num -= 1
            # Imprime el factorial del número
            print("Factorial ",n,"! es ", fact)  

# Comprueba si se proporcionaron suficientes argumentos
if len(sys.argv) <= 1:
   # Si no se proporcionaron suficientes argumentos, imprime un mensaje de error y sale del programa
   print("Debe informar un rango de números!")
   sys.exit()

# Obtiene el rango de los argumentos
rango = sys.argv[1]
# Comprueba si el rango contiene un '-'
if '-' in rango:
    # Divide el rango en 'desde' y 'hasta'
    desde, hasta = rango.split('-')
    # Si 'desde' está vacío, lo establece en 1
    if desde == '':
        desde = 1
    else:
        # Convierte 'desde' en un entero
        desde = int(desde)
    # Si 'hasta' está vacío, lo establece en 60
    if hasta == '':
        hasta = 60
    else:
        # Convierte 'hasta' en un entero
        hasta = int(hasta)
else:
    # Si no hay '-' en el rango, establece 'desde' en 1 y 'hasta' en el valor del rango
    desde = 1
    hasta = int(rango)

# Llama a la función factorial con los argumentos desde y hasta
factorial(desde, hasta)
