import heapq

def beautiful_path(n, m, s, d, weights, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)

    cost = [float('inf')] * (n + 1)
    cost[s] = weights[s - 1]  
    pq = [(cost[s], s)]  

    while pq:
        curr_cost, u = heapq.heappop(pq)
        if curr_cost > cost[u]:
            continue
        for v in graph[u]:
            new_cost = curr_cost + weights[v - 1]
            if new_cost < cost[v]:
                cost[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return cost[d] if cost[d] != float('inf') else -1

def main():
    n, m, s, d = map(int, input().split())
    weights = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    result = beautiful_path(n, m, s, d, weights, edges)
    print(result)


main()
