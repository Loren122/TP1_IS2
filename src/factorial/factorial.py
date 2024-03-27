#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(desde, hasta): 
    for num in range(desde, hasta+1):
        if num < 0: 
            print("Factorial de un número negativo no existe")
        elif num == 0: 
            print("Factorial de 0 es 1")
        else: 
            fact = 1
            n = num  # Guarda el valor original de num
            while(num > 1): 
                fact *= num 
                num -= 1
            print("Factorial ",n,"! es ", fact)  # Imprime el valor original de num

if len(sys.argv) <= 2:
   print("Debe informar un rango de números!")
   sys.exit()

desde = int(sys.argv[1])
hasta = int(sys.argv[2])

factorial(desde, hasta)

