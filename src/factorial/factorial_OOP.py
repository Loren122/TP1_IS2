import sys

class Factorial:
    # Constructor de la clase
    def __init__(self):
        pass

    # Método run que toma dos argumentos: min y max
    def run(self, min, max): 
        # Itera sobre cada número en el rango desde 'min' hasta 'max' inclusive
        for num in range(min, max+1):
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
if len(sys.argv) <= 2:
   # Si no se proporcionaron suficientes argumentos, imprime un mensaje de error y sale del programa
   print("Debe informar un rango de números!")
   sys.exit()

# Convierte los argumentos en enteros
min = int(sys.argv[1])
max = int(sys.argv[2])

# Crea una instancia de la clase Factorial
factorial = Factorial()
# Llama al método run de la clase Factorial con los argumentos min y max
factorial.run(min, max)

