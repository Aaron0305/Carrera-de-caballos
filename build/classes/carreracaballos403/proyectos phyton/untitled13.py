# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:58:55 2024

@author: DELL
"""

print("***********************************************************************************************")
print("Programa para calcular, Precisión, Sesgo, Exactitud e Incertidumbre")
print("")
print("Ejemplo de cómo usar este programa \n")
print("Supongamos que tenemos los siguientes datos:")
print("Pares de datos:                 3")
print("Valores reales:      85   92   78")
print("Valores predichos:   83   90   80")
print("Para usar este programa, introduce los datos reales y los predichos cuando se te solicite.")
print("***********************************************************************************************")
import numpy as np
n_datos = int(input("Introduce el número de pares de datos: "))
valores_verdaderos = []
valores_predichos = []
for i in range(n_datos):
    real = float(input(f"Ingresa el valor real para el dato {i+1}: "))
    predicho = float(input(f"Ingresa el valor predicho para el dato {i+1}: "))
    valores_verdaderos.append(real)
    valores_predichos.append(predicho)


valores_verdaderos = np.array(valores_verdaderos)# Convertir las listas a arrays de NumPy 
valores_predichos = np.array(valores_predichos)
sesgo = np.mean(valores_predichos - valores_verdaderos)# Realizar los cálculos
exactitud = np.mean(np.abs(valores_verdaderos - valores_predichos))
precision = np.sqrt(np.mean((valores_verdaderos - valores_predichos) ** 2))
incertidumbre = 1.96 * np.std(valores_verdaderos - valores_predichos)

print("")
print("Precisión:", precision)
print("Sesgo:", sesgo)
print("Exactitud:", exactitud)
print("Incertidumbre:", incertidumbre)
