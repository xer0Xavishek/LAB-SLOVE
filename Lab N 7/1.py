import heapq

def shortest_pth():
    N, M, S, D = map(int, input().split())
    ul = list(map(int, input().split()))
    vl = list(map(int, input().split()))
    wl = list(map(int, input().split()))

    gr = [[] for _ in range(N + 1)]
    for i in range(M):
        u, v, w = ul[i], vl[i], wl[i]
        gr[u].append((v, w))
    
    ds = [float('inf')] * (N + 1)
    par = [-1] * (N + 1)
    ds[S] = 0
    pq = [(0, S)]  
    while pq:
        d, u = heapq.heappop(pq)
        if d > ds[u]:
            continue
        for v, w in gr[u]:
            if ds[v] > d + w:
                ds[v] = d + w
                par[v] = u
                heapq.heappush(pq, (ds[v], v))
    
    if ds[D] == float('inf'):
        print(-1)
        return

    pth = []
    crr = D
    while crr != -1:
        pth.append(crr)
        crr = par[crr]
    pth.reverse()

    print(ds[D])
    print(" ".join(map(str, pth)))

shortest_pth()





