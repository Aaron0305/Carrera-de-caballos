import random

# Genera un arreglo de 100,000 elementos no repetidos
arr = random.sample(range(1, 200001), 100000)

# Aplica el método de ordenamiento incorporado
arr_ordenado = sorted(arr)

# Muestra los primeros 10 elementos ordenados
print("Primeros 10 elementos ordenados:")
print(arr_ordenado[:100000])
