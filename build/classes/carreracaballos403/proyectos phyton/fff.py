# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:59:37 2023

@author: DELL
"""
import numpy as np
import pandas as pd

def vogel_method(costs, supply, demand):
    num_sources, num_destinations = len(supply), len(demand)
    allocations = np.zeros((num_sources, num_destinations))
    
    while np.sum(allocations) < np.sum(demand):
        row_penalties = []
        col_penalties = []
        
        # Calcular las penalizaciones de fila y columna
        for i in range(num_sources):
            row = costs[i, :]
            min1, min2 = np.partition(row, 2)[:2]
            row_penalties.append(abs(min1 - min2))
        
        for j in range(num_destinations):
            col = costs[:, j]
            min1, min2 = np.partition(col, 2)[:2]
            col_penalties.append(abs(min1 - min2))
        
        max_row_penalty = max(row_penalties)
        max_col_penalty = max(col_penalties)
        
        if max_row_penalty >= max_col_penalty:
            source_index = row_penalties.index(max_row_penalty)
            min_cost_index = np.argmin(costs[source_index, :])
            allocation = min(supply[source_index], demand[min_cost_index])
            allocations[source_index, min_cost_index] = allocation
            supply[source_index] -= allocation
            demand[min_cost_index] -= allocation
        else:
            dest_index = col_penalties.index(max_col_penalty)
            min_cost_index = np.argmin(costs[:, dest_index])
            allocation = min(supply[min_cost_index], demand[dest_index])
            allocations[min_cost_index, dest_index] = allocation
            supply[min_cost_index] -= allocation
            demand[dest_index] -= allocation
    
    return allocations

# Solicitar entrada de datos al usuario
num_sources = int(input("Número de fuentes (filas): "))
num_destinations = int(input("Número de destinos (columnas): "))

costs = np.zeros((num_sources, num_destinations))
for i in range(num_sources):
    for j in range(num_destinations):
        costs[i, j] = int(input(f"Costo de la fuente {i+1} al destino {j+1}: "))

supply = []
for i in range(num_sources):
    supply.append(int(input(f"Oferta de la fuente {i+1}: ")))

demand = []
for j in range(num_destinations):
    demand.append(int(input(f"Demande del destino {j+1}: ")))

# Aplicar el método Vogel
allocations = vogel_method(costs, supply, demand)

# Calcular el costo total
total_cost = np.sum(allocations * costs)

# Crear un DataFrame de pandas para mostrar los datos ingresados
data = {'Fuente': ['Fuente {}'.format(i + 1) for i in range(num_sources)],
        'Oferta': supply}
df_input = pd.DataFrame(data)
df_input.set_index('Fuente', inplace=True)

data = {'Destino': ['Destino {}'.format(j + 1) for j in range(num_destinations)],
        'Demanda': demand}
df_demand = pd.DataFrame(data)
df_demand.set_index('Destino', inplace=True)

df_cost = pd.DataFrame(costs, index=df_input.index, columns=df_demand.index)

print("Datos Ingresados:")
print(df_input)
print("\n")
print("Costos de Transporte:")
print(df_cost)
print("\n")
print("Demandas:")
print(df_demand)
print("\n")

# Calcular penalizaciones
row_penalties = []
col_penalties = []

for i in range(num_sources):
    row = costs[i, :]
    min1, min2 = np.partition(row, 2)[:2]
    row_penalties.append(abs(min1 - min2))

for j in range(num_destinations):
    col = costs[:, j]
    min1, min2 = np.partition(col, 2)[:2]
    col_penalties.append(abs(min1 - min2))

df_row_penalties = pd.DataFrame(row_penalties, index=df_input.index, columns=['Penalización de Fila'])
df_col_penalties = pd.DataFrame(col_penalties, index=df_demand.index, columns=['Penalización de Columna'])

print("Penalizaciones de Fila:")
print(df_row_penalties)
print("\n")

print("Penalizaciones de Columna:")
print(df_col_penalties)
print("\n")

# Crear un DataFrame de pandas para mostrar las asignaciones óptimas
df_allocations = pd.DataFrame(allocations, index=df_input.index, columns=df_demand.index)

print("Asignaciones óptimas:")
print(df_allocations)
print("\n")

# Mostrar el costo total
print(f"Costo Total Mínimo (Zmin): {total_cost}")
