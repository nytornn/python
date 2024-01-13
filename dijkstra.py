import heapq

def dijkstra(graph, start):
    # Initialize distances and predecessor
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

graph = {
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'D': 4, 'E': 2},
    'C': {'E': 5},
    'D': {'A': 3, 'B': 4, 'E': 1},
    'E': {'B': 2, 'C': 5, 'D': 1}
}

start_vertex = 'C'
result = dijkstra(graph, start_vertex)
print(f"Shortest distances from {start_vertex}: {result}")