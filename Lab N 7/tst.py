import heapq

def pe():
    n, m = map(int, input().split())
    ul = list(map(int, input().split()))
    vl = list(map(int, input().split()))
    wl = list(map(int, input().split()))
    
    g = [[] for _ in range(n + 1)]
    for u, v, w in zip(ul, vl, wl):
        g[u].append((v, w))

    d = [[float('inf')] * 2 for _ in range(n + 1)]


    pq = []

    for v, w in g[1]:
        p = w % 2
        if w < d[v][p]:


            d[v][p] = w
            heapq.heappush(pq, (w, v, p))

    while pq:
        cst, nd, par = heapq.heappop(pq)
        if cst > d[nd][par]:
            continue
        for nei, w in g[nd]:
            new_par = w % 2
            if new_par != par:
                new_cst = cst + w
                if new_cst < d[nei][new_par]:
                    d[nei][new_par] = new_cst
                    heapq.heappush(pq, (new_cst, nei, new_par))

    ans = min(d[n][0], d[n][1])
    print(ans if ans != float('inf') else -1)
pe()