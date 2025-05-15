import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def main():
    N, M, S, T = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    dist_S = dijkstra(N, graph, S)
    dist_T = dijkstra(N, graph, T)

    min_time = float('inf')
    meet_node = -1
    for i in range(1, N + 1):
        if dist_S[i] != float('inf') and dist_T[i] != float('inf'):
            time = max(dist_S[i], dist_T[i])
            if time < min_time or (time == min_time and i < meet_node):
                min_time = time
                meet_node = i

    if meet_node == -1:
        print(-1)
    else:
        print(f"{min_time} {meet_node}")

main()
