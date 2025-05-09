import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u - 1, v - 1))

edges.sort()

parr = list(range(n))
s = [1] * n

def find(u):
    while parr[u] != u:
        parr[u] = parr[parr[u]]
        u = parr[u]
    return u

def union(u, v):
    u, v = find(u), find(v)
    if u == v:
        return False
    if s[u] < s[v]:
        u, v = v, u
    parr[v] = u
    s[u] += s[v]
    return True

mst_cost = 0
mst_edges = []

for w, u, v in edges:
    if union(u, v):
        mst_cost += w
        mst_edges.append((w, u, v))

if len(mst_edges) != n - 1:
    print(-1)
    exit()

from collections import defaultdict, deque

adj = defaultdict(list)
for w, u, v in mst_edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

LOG = 11
par = [[-1] * n for _ in range(LOG)]
max_wt = [[0] * n for _ in range(LOG)]
depth = [0] * n

def bfs(root):
    visited = [False] * n
    queue = deque([root])
    visited[root] = True
    while queue:
        u = queue.popleft()

        for v, w in adj[u]:

            if not visited[v]:
                
                visited[v] = True
                par[0][v] = u
                max_wt[0][v] = w
                depth[v] = depth[u] + 1
                queue.append(v)

bfs(0)

for i in range(1, LOG):
    for v in range(n):
        if par[i-1][v] != -1:
            par[i][v] = par[i-1][par[i-1][v]]
            max_wt[i][v] = max(max_wt[i-1][v], max_wt[i-1][par[i-1][v]])

def get_max(u, v):

    if depth[u] < depth[v]:

        u, v = v, u

    res = 0

    for i in reversed(range(LOG)):

        if depth[u] - (1 << i) >= depth[v]:

            res = max(res, max_wt[i][u])
            u = par[i][u]
    if u == v:

        return res
    
    for i in reversed(range(LOG)):

        if par[i][u] != -1 and par[i][u] != par[i][v]:
            res = max(res, max_wt[i][u], max_wt[i][v])
            u = par[i][u]

            v = par[i][v]

    return max(res, max_wt[0][u], max_wt[0][v])

mes = set((min(u, v), max(u, v), w) for w, u, v in mst_edges)
sbst = float('inf')

for w, u, v in edges:

    key = (min(u, v), max(u, v), w)
    if key in mes:
        continue
    max_in_path = get_max(u, v)
    if max_in_path != w:
        sbst = min(sbst, mst_cost + w - max_in_path)

print(sbst if sbst < float('inf') else -1)
