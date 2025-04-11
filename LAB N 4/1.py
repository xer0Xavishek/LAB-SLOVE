n, m = map(int, input().split())
adj_mtx = [[0] * n for p in range(n)]
for k in range(m):
    u, v, w = map(int, input().split())
    adj_mtx[u-1][v-1] = w

for row in adj_mtx:
    print(' '.join(map(str, row)) + ' ')