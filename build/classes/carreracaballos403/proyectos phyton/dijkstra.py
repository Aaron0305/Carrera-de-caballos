import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def find_shortest_path(graph, start, end):
    # Aplicar el algoritmo de Dijkstra
    distances = dijkstra(graph, start)
    
    # Calcular el costo mínimo y la ruta mínima
    cost_min = distances[end]
    path_min = [end]
    current_vertex = end

    while current_vertex != start:
        for neighbor, weight in graph[current_vertex].items():
            if distances[current_vertex] == distances[neighbor] + weight:
                path_min.insert(0, neighbor)
                current_vertex = neighbor
                break

    return cost_min, path_min

# Definir el grafo
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

# Elegir el nodo de inicio y destino
start_node = 'A'
end_node = 'J'

# Calcular el costo mínimo y la ruta mínima
cost_min, path_min = find_shortest_path(graph, start_node, end_node)

# Imprimir los resultados
print(f"Origen: {start_node}")
print(f"Destino: {end_node}")
print(f"Costo Mínimo: {cost_min}")
print(f"Ruta Mínima: {' -> '.join(path_min)}")
