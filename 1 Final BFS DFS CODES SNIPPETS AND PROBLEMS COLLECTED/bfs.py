def bfs(graph, start):
    # Initialization
    color = {}         # 'WHITE', 'GRAY', 'BLACK'
    distance = {}      # Distance from start node
    predecessor = {}   # Parent node in BFS tree
    traversal_order = []  # Order of visited nodes

    for node in graph:
        color[node] = 'WHITE'
        distance[node] = float('inf')
        predecessor[node] = None

    color[start] = 'GRAY'
    distance[start] = 0
    queue = [start]  # Simple list used as queue

    while queue:
        u = queue.pop(0)  # Dequeue
        traversal_order.append(u)
        for v in graph[u]:
            if color[v] == 'WHITE':
                color[v] = 'GRAY'
                distance[v] = distance[u] + 1
                predecessor[v] = u
                queue.append(v)  # Enqueue
        color[u] = 'BLACK'

    # Output
    print("Traversal Order:", traversal_order)
    print("Distance:", distance)
    print("Predecessor:", predecessor)
    return distance, predecessor




graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')

# Output:Traversal Order: ['A', 'B', 'C', 'D', 'E', 'F']
# Distance: {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}
# Predecessor: {'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'B', 'F': 'C'}
# The BFS function performs a breadth-first search on the graph starting from the given node.