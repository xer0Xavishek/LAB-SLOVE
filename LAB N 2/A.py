def twoSumTrouble(n,s,arr):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == s:
                return f"{i+1} {j+1}"
    return -1

n,s = map(int,input().split())
arr = list(map(int,input().split()))
print(twoSumTrouble(n,s,arr))