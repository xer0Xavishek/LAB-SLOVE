def dfs(graph):
    color = {}
    predecessor = {}
    discovery = {}
    finish = {}
    traversal_order = []
    time = {'value': 0}  # Use a dictionary to manage time as a shared mutable object

    # Initialization
    for u in graph:
        color[u] = 'WHITE'
        predecessor[u] = None

    # DFS
    for u in graph:
        if color[u] == 'WHITE':
            dfs_visit(graph, u, color, predecessor, discovery, finish, time, traversal_order)

    return discovery, finish, predecessor


def dfs_visit(graph, u, color, predecessor, discovery, finish, time, traversal_order):
    color[u] = 'GRAY'
    time['value'] += 1
    discovery[u] = time['value']

    for v in graph[u]:
        if color[v] == 'WHITE':
            predecessor[v] = u
            dfs_visit(graph, v, color, predecessor, discovery, finish, time, traversal_order)

    color[u] = 'BLACK'
    time['value'] += 1
    finish[u] = time['value']
    traversal_order.append(u)


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

discovery, finish, predecessor = dfs(graph)
print("Discovery Times:", discovery)
print("Finish Times:", finish)
print("Predecessors:", predecessor)