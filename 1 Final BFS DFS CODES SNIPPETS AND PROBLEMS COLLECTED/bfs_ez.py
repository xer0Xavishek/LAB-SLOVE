def bfs(graph, start):
    color = {node: 'WHITE' for node in graph}  # WHITE = unvisited, GREY = in queue, BLACK = fully explored
    queue = [start]
    traversal_order = []

    color[start] = 'GREY'

    while queue:
        u = queue.pop(0)  # dequeue
        traversal_order.append(u)
        print(u)

        for v in graph[u]:  # for each vertex v ∈ Adj[u]
            if color[v] == 'WHITE':
                color[v] = 'GREY'
                queue.append(v)  # enqueue

        color[u] = 'BLACK'  # fully explored

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

bfs(graph, 'A')
