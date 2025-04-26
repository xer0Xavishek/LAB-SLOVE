def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    indeg = [0] * (N + 1)
    
    for v in range(M):
        A, B = map(int, input().split())
        adj[A].append(B)
        indeg[B] += 1
    
    Q = []
    for i in range(1, N + 1):
        if indeg[i] == 0:
            Q.append(i)
    
    topOrd = []
    while Q:
        u = Q.pop(0)
        topOrd.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                Q.append(v)
    
    if len(topOrd) == N:
        print(' '.join(map(str, topOrd)))
    else:
        print(-1)

if __name__ == "__main__":
    main()