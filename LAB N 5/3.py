N, M, S, D = map(int, input().split())

adj = [[] for k in range(N + 1)]

uL = list(map(int, input().split()))

vL = list(map(int, input().split()))

for i in range(M):

    u = uL[i]

    v = vL[i]

    adj[u].append(v)

    adj[v].append(u)

for i in range(1, N + 1):

    adj[i].sort()


dist = [float('inf')] * (N + 1)

par = [-1] * (N + 1)

Q = []

dist[S] = 0

Q.append(S)

found = False

while Q:

    u = Q.pop(0)

    if u == D:

        found = True

        break

    for v in adj[u]:

        if dist[v] == float('inf'):

            dist[v] = dist[u] + 1

            par[v] = u

            Q.append(v)

        elif dist[v] == dist[u] + 1:

            if par[v] > u:

                par[v] = u


if not found:

    print(-1)
else:

    path = []

    current = D

    while current!=1:

        path.append(current)

        current = par[current]
    path.reverse()

    print(len(path) - 1)

    print(' '.join(map(str, path)))