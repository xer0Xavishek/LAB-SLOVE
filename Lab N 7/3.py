import heapq

def minimize_danger(n, roads):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))  
    danger = [float('inf')] * (n + 1)
    danger[1] = 0
    pq = [(0, 1)]  

    while pq:
        curr_danger, u = heapq.heappop(pq)
        if curr_danger > danger[u]:
            continue
        for v, w in graph[u]:
            new_danger = max(curr_danger, w)
            if new_danger < danger[v]:
                danger[v] = new_danger
                heapq.heappush(pq, (new_danger, v))

    result = [0 if i == 1 else (danger[i] if danger[i] != float('inf') else -1) for i in range(1, n + 1)]
    return result

def main():
    n, m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    result = minimize_danger(n, roads)
    print(' '.join(map(str, result)))

main()
