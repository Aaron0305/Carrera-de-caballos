# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:36:17 2024

@author: DELL
"""

import numpy as np

# Función para calcular la aproximación, precisión, sesgo y exactitud
def calculate_metrics(true_values, predicted_values):
    # Calculando la aproximación
    approximation = np.mean(predicted_values)
    
    # Calculando la precisión
    precision = np.std(predicted_values)
    
    # Calculando el sesgo
    bias = np.mean(true_values - predicted_values)
    
    # Calculando la exactitud
    accuracy = np.mean(np.abs(true_values - predicted_values))
    
    return approximation, precision, bias, accuracy

# Solicitar los datos al usuario
num_data_points = int(input("¿Cuántos datos tiene? "))

true_values = []
predicted_values = []

print("Ingresa los valores reales:")
for i in range(num_data_points):
    value = float(input(f"Valor {i+1}: "))
    true_values.append(value)

print("Ingresa los valores predichos:")
for i in range(num_data_points):
    value = float(input(f"Valor {i+1}: "))
    predicted_values.append(value)

# Convertir a arrays de NumPy
true_values = np.array(true_values)
predicted_values = np.array(predicted_values)

# Calcular y mostrar los resultados
approximation, precision, bias, accuracy = calculate_metrics(true_values, predicted_values)

print("Aproximación:", approximation)
print("Precisión:", precision)
print("Sesgo:", bias)
print("Exactitud:", accuracy)