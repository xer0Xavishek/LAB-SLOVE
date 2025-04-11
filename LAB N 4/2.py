
n, m = map( int, input().split())


u = list( map(int, input().split()))
v = list( map(int, input().split()))
w = list( map(int, input().split()))

adj_list = [[] for p in range(n + 1)]  

for i in range(m):

    src = u[i]

    dest = v[i]

    weight = w[i]

    adj_list[src].append((dest, weight))

for nd in range(1, n + 1):

    edges = adj_list[nd]

    res = f"{nd}:"

    for d, w in edges:
        res += f" ({d},{w})"
    print(res)