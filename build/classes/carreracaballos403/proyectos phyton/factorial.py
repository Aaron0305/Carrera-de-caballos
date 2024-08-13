# aaron estrada
"""
Created on Thu Sep 14 18:21:52 2023

@author: DELL
"""
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Ejemplo de uso:
n = 5  # Cambia este valor para calcular el factorial de otro número
resultado = factorial(n)
print(f"El factorial de {n} es: {resultado}")