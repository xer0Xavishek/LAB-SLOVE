

n = int(input())

adj_m = [[0] * n for p in range(n)]




for i in range(n):

    frg = list(map(int, input().split()))

    k = frg[0]

    nei = frg[1:]


    for j in nei:
        adj_m[i][j] = 1






for row in adj_m:
    print(' '.join(map(str, row)) + ' ')