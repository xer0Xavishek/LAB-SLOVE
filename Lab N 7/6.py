import sys
import heapq

def main():
    input = sys.stdin.readline
    INF = 10**30

    n, m, S, D = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    dist = [[INF, INF] for _ in range(n+1)]
    dist[S][0] = 0

    pq = [(0, S)]  
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u][1]:
            continue
        
        for v, w in adj[u]:
            d2 = d + w
            if d2 < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = d2
                heapq.heappush(pq, (d2, v))
                if dist[v][1] < INF:
                    heapq.heappush(pq, (dist[v][1], v))
            elif dist[v][0] < d2 < dist[v][1]:
                dist[v][1] = d2
                heapq.heappush(pq, (d2, v))

    ans = dist[D][1]
    print(ans if ans < INF else -1)

if __name__ == "__main__":
    main()
