#!/usr/bin/python3
# Python program to display all the prime numbers within an interval.

# Se definen los límites inferior y superior para buscar números primos.
lower = 1
upper = 100

# Se imprime un mensaje para indicar el rango en el que vamos a buscar.
print("Prime numbers between", lower, "and", upper, "are:")


# Se itera sobre cada número en el rango definido.
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1.
   if num > 1:
       for i in range(2, num):
           # Si se encuentra un divisor, entonces el número no es primo y sale del bucle.
           if (num % i) == 0:
               break
       else:
           # Si no se encuentra un divisor, el número se imprime.
           print(num)
