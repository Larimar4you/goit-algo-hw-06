"""Завдання 3

Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
"""

graph_weighted = {
    "A": {"B": 2, "C": 4},
    "B": {"A": 2, "C": 1, "D": 7},
    "C": {"A": 4, "B": 1, "E": 3},
    "D": {"B": 7, "E": 2, "F": 1},
    "E": {"C": 3, "D": 2, "F": 5},
    "F": {"D": 1, "E": 5},
}


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


# Застосування до всіх вершин
all_shortest_paths = {}
for node in graph_weighted.keys():
    all_shortest_paths[node] = dijkstra(graph_weighted, node)

# Виведення
for start, distances in all_shortest_paths.items():
    print(f"Відстані від вершини {start}: {distances}")
