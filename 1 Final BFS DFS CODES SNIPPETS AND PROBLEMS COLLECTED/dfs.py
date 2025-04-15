def dfs(graph):
    color = {}
    predecessor = {}
    discovery = {}
    finish = {}
    time = [0]
    traversal_order = []

    # Initialization
    for u in graph:
        color[u] = 'WHITE'
        predecessor[u] = None

    # DFS
    for u in graph:
        if color[u] == 'WHITE':
            dfs_visit(graph, u, color, predecessor, discovery, finish, time, traversal_order)

    # Output
    print("Traversal Order:", traversal_order)
    print("Discovery Time:", discovery)
    print("Finish Time:", finish)
    print("Predecessor:", predecessor)
    return discovery, finish, predecessor


def dfs_visit(graph, u, color, predecessor, discovery, finish, time, traversal_order):
    color[u] = 'GRAY'
    time[0] += 1
    discovery[u] = time[0]

    for v in graph[u]:
        if color[v] == 'WHITE':
            predecessor[v] = u
            dfs_visit(graph, v, color, predecessor, discovery, finish, time, traversal_order)

    color[u] = 'BLACK'
    time[0] += 1
    finish[u] = time[0]
    traversal_order.append(u)


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

dfs(graph)


# Output: