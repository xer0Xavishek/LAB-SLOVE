
n, m = map(int, input().split())
adj   = [[] for h in range(n+1)]
indg = [0]  * (n+1)

for k in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    indg[v] += 1

q = []
hd = 0
for u in range(1, n+1):
    if indg[u] == 0:
        q.append(u)

cnt = 0
while hd < len(q):
    u = q[hd]
    hd += 1
    cnt += 1
    for v in adj[u]:
        indg[v] -= 1
        if indg[v] == 0:
            q.append(v)

print("YES" if cnt != n else "NO")
