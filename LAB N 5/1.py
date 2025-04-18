FL = input().split()
N = int(FL[0])
M = int(FL[1])

adj = [[] for n in range(N + 1)]

for i in range(M):

    u, v = map(int, input().split())

    adj[u].append(v)
    
    adj[v].append(u)

vs = [False] * (N + 1)
Q = []
Q.append(1)
vs[1] = True
result = []

while Q:


    u = Q.pop(0)


    result.append(str(u))


    for v in (adj[u]):

        if not vs[v]:

            vs[v] = True

            Q.append(v)

print(' '.join(result))