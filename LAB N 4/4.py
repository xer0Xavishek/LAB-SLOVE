
N,M = map(int,input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))

deg = [0] * (N + 1)

for i in range(M):

    a = u[i]

    b = v[i]

    deg[a] += 1
    deg[b] += 1

oddTrackk = 0



for i in range(1, N + 1):

    if deg[i] % 2 != 0:

        oddTrackk += 1

if oddTrackk == 0 or oddTrackk == 2:

    print("YES")
    
else:
    print("NO")
