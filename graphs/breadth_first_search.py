graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
queue = []


def bfs(graph, visited, node):
    visited.append(node)
    queue.append(node)

    while queue:
        current = queue.pop()
        neighbors = graph[current]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    print(visited)
