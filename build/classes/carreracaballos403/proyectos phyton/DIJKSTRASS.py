# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 15:29:53 2023

@author: DELL
"""

# -*- coding: utf-8 -*-
import heapq

def dijkstra(graph, start):
    if start not in graph:
        raise ValueError("El nodo de inicio no está en el grafo")

    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 3, 'C': 8, 'D': 5},
    'B': {'A': 3, 'C': 5, 'F': 7},
    'C': {'A': 8, 'B': 5, 'D': 2, 'E': 8, 'F': 5},
    'D': {'A': 5, 'C': 2, 'G': 4},
    'E': {'C': 8, 'F': 5, 'G': 6, 'H': 1, 'I': 3},
    'F': {'B': 7, 'C': 5, 'E': 5, 'H': 6},
    'G': {'D': 4, 'E': 6, 'I': 4},
    'H': {'E': 1, 'F': 6, 'J': 2},
    'I': {'E': 3, 'G': 4, 'J': 6},
    'J': {'H': 2, 'I': 6}, 
    }

start_node = 'A'

try:
    result = dijkstra(graph, start_node)
    for node, distance in result.items():
        print(f"Distancia de {start_node} a {node} = {distance}")
except ValueError as e:
    print(f"Error: {e}")
