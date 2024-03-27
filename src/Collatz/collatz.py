import matplotlib.pyplot as plt

def collatz(n):
    # Inicializa el contador de pasos
    pasos = 0
    while n != 1:
        # Aplica las reglas de la conjetura de Collatz
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        pasos += 1
    return pasos

# Inicializa las listas para almacenar los resultados
nums = []
iterations = []

# Calcula la secuencia de Collatz para cada número entre 1 y 10000
for i in range(1, 10001):
    nums.append(i)
    iterations.append(collatz(i))

# Crea un gráfico de los resultados
plt.figure(figsize=(10, 6))
plt.scatter(nums, iterations, s=1)
plt.title('Número de iteraciones de la conjetura de Collatz')
plt.xlabel('Número inicial')
plt.ylabel('Número de iteraciones hasta llegar a 1')
plt.show()
