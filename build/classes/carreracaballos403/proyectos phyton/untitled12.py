import numpy as np

# Función para calcular la incertidumbre, precisión, sesgo y exactitud
def calculate_metrics(true_values, predicted_values):
    # Calculando la precisión
    precision = np.std(predicted_values)
    
    # Calculando el sesgo
    bias = np.mean(true_values - predicted_values)
    
    # Calculando la exactitud
    accuracy = np.mean(np.abs(true_values - predicted_values))
    
    # Calculando la incertidumbre
    uncertainty = 1.96 * precision
    
    return precision, bias, accuracy, uncertainty

# Solicitar los datos al usuario
num_data_points = int(input("¿Cuántos pares de datos tiene? "))

true_values = []
predicted_values = []

print("Ingresa los valores reales y predichos:")
for i in range(num_data_points):
    true_value = float(input(f"Valor real {i+1}: "))
    predicted_value = float(input(f"Valor predicho {i+1}: "))
    true_values.append(true_value)
    predicted_values.append(predicted_value)

# Convertir a arrays de NumPy
true_values = np.array(true_values)
predicted_values = np.array(predicted_values)

# Calcular y mostrar los resultados
precision, bias, accuracy, uncertainty = calculate_metrics(true_values, predicted_values)

print("Precisión:", precision)
print("Sesgo:", bias)
print("Exactitud:", accuracy)
print("Incertidumbre:", uncertainty)