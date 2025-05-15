import heapq

def parity_edges():
    n, m = map(int, input().split())
    u_list = list(map(int, input().split()))
    v_list = list(map(int, input().split()))
    w_list = list(map(int, input().split()))
    
    graph = [[] for _ in range(n + 1)]
    for u, v, w in zip(u_list, v_list, w_list):
        graph[u].append((v, w))

    dist = [[float('inf')] * 2 for _ in range(n + 1)]
    pq = []

    for v, w in graph[1]:
        p = w % 2
        if w < dist[v][p]:
            dist[v][p] = w
            heapq.heappush(pq, (w, v, p))

    while pq:
        cost, node, parity = heapq.heappop(pq)
        if cost > dist[node][parity]:
            continue
        for nei, w in graph[node]:
            new_parity = w % 2
            if new_parity != parity:
                new_cost = cost + w
                if new_cost < dist[nei][new_parity]:
                    dist[nei][new_parity] = new_cost
                    heapq.heappush(pq, (new_cost, nei, new_parity))

    ans = min(dist[n][0], dist[n][1])
    print(ans if ans != float('inf') else -1)
parity_edges()