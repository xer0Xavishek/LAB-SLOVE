def main():
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    colr = [-1] * (N + 1)
    maxg = 0
    
    for i in range(1, N + 1):
        if colr[i] == -1:
            Q = []
            Q.append(i)
            colr[i] = 0
            count = [0, 0]
            count[0] += 1
            while Q:
                u = Q.pop(0)
                for v in adj[u]:
                    if colr[v] == -1:
                        colr[v] = colr[u] ^ 1
                        count[colr[v]] += 1
                        Q.append(v)
                    elif colr[v] == colr[u]:
                        pass
            maxg += max(count)
    
    print(maxg)

if __name__ == "__main__":
    main()