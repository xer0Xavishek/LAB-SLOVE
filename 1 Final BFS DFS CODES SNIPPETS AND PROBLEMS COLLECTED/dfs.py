def dfs(graph):
    color = {'WHITE' for node in graph}  # WHITE = unvisited, GRAY = discovered, BLACK = finished
    predecessor = {None for node in graph}  # Initialize predecessor for all nodes
    discovery = {} # Discovery time for each node
    finish = {} # Finish time for each node
    traversal_order = [] # To keep track of the order of traversal
    time = [0]  # Use a list to manage time as a mutable object

    # DFS
    for u in graph:
        if color[u] == 'WHITE':
            dfs_visit(graph, u, color, predecessor, discovery, finish, time, traversal_order)

    return discovery, finish, predecessor


def dfs_visit(graph, u, color, predecessor, discovery, finish, time, traversal_order):
    color[u] = 'GRAY'
    time[0] += 1  # Increment time
    discovery[u] = time[0]

    for v in graph[u]:
        if color[v] == 'WHITE':
            predecessor[v] = u
            dfs_visit(graph, v, color, predecessor, discovery, finish, time, traversal_order)

    color[u] = 'BLACK'
    time[0] += 1  # Increment time
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

discovery, finish, predecessor = dfs(graph)
print("Discovery Times:", discovery)
print("Finish Times:", finish)
print("Predecessors:", predecessor)