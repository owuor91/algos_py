graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()


def dfs(graph, visited, node):
    if node not in visited:
        visited.add(node)
        print(node)
        neighbors = graph[node]
        for neighbor in neighbors:
            dfs(graph, visited, neighbor)
