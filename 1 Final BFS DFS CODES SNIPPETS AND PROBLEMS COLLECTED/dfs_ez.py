def dfs(graph, start):
    color = {node: 'WHITE' for node in graph}  # WHITE = unvisited, GREY = discovered, BLACK = finished
    stack = [start]
    traversal_order = []

    while stack:
        u = stack.pop()

        if color[u] == 'WHITE':
            color[u] = 'GREY'
            traversal_order.append(u)
            print(u)

            # Push the current node back to finish after its neighbors
            stack.append(u)

            # Push unvisited neighbors in reverse order
            for v in reversed(graph[u]):
                if color[v] == 'WHITE':
                    stack.append(v)
        
        elif color[u] == 'GREY':
            color[u] = 'BLACK'

    return traversal_order


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

dfs(graph, 'A')
