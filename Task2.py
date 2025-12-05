"""Завдання 2

Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі, який було розроблено у першому завданні.

Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.
"""

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "E"],
    "D": ["B", "E", "F"],
    "E": ["C", "D", "F"],
    "F": ["D", "E"],
}


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(reversed(graph[vertex]))  # реверс для "правильного" обходу
    return path


def bfs_iterative(graph, start):
    visited = set([start])
    queue = deque([start])
    path = []

    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return path


start_node = "A"

dfs_path = dfs_iterative(graph, start_node)
bfs_path = bfs_iterative(graph, start_node)

print("DFS path:", dfs_path)
print("BFS path:", bfs_path)
