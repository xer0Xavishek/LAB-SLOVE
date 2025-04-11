def pMAX(A, l, h):
    if h == l:
        return -1
    if h - l == 1:

        return A[l] + A[h] ** 2 

    m = (l + h) // 2
    
    l_mxxx = pMAX(A, l, m)

    r_maxx = pMAX(A, m + 1, h)
    
    l_mx_val = max(A[l:m+1])
    
    res = max(l_mxxx, r_maxx)
    
    for j in range(m + 1, h + 1):
        
        res = max(res, l_mx_val + A[j] ** 2)
    
    return res

def solve(N, A):

    return pMAX(A, 0, N - 1)

N = int(input())

A = list(map(int, input().split()))

print(solve(N, A))
