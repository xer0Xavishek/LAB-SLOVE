def gcd(a, b):

    while b:

        a, b = b, a % b

    return a


N,Q = map(int,input().split())


adj = [[] for p in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j and gcd(i, j) == 1:
            adj[i].append(j)

for i in range(1, N + 1):
    adj[i].sort()

res = []
for z in range(Q):

    X, K = map(int, input().split())

    nei = adj[X]
    
    if K <= len(nei):
        res.append(str(nei[K - 1]))
    else:
        res.append("-1")

print('\n'.join(res))

