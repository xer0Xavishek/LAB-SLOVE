N,M=map( int,input().split())

u=list( map(int, input().split()))

v=list( map(int, input().split()))

indg=[0] * (N + 1)
outdg=[0] * (N + 1)

for i in range(M):

    a =u[i]
    b =v[i]
    outdg[a]+= 1
    indg[b]+= 1

result = []


for i in range(1, N + 1):
    
    result.append(str(indg[i] - outdg[i]))

print(' '.join(result))