def dfs(graph):
    color = {}
    predecessor = {}
    discovery = {}
    finish = {}
    traversal_order = []

    # Initialization
    for u in graph:
        color[u] = 'WHITE'
        predecessor[u] = None

    time = 0  # Use an integer for time

    # DFS
    for u in graph:
        if color[u] == 'WHITE':
            time = dfs_visit(graph, u, color, predecessor, discovery, finish, time, traversal_order)

    return discovery, finish, predecessor


def dfs_visit(graph, u, color, predecessor, discovery, finish, time, traversal_order):
    color[u] = 'GRAY'
    time += 1
    discovery[u] = time

    for v in graph[u]:
        if color[v] == 'WHITE':
            predecessor[v] = u
            time = dfs_visit(graph, v, color, predecessor, discovery, finish, time, traversal_order)

    color[u] = 'BLACK'
    time += 1
    finish[u] = time
    traversal_order.append(u)

    return time  # Return the updated time


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