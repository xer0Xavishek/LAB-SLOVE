def twoSumTrouble(n, s, arr):
    dkt = {}
    for i in range(n):
        var = s - arr[i]
        if var in dkt:
            return f"{dkt[var]+1} {i+1}"
        dkt[arr[i]] = i
    return -1

n, s = map(int, input().split())
arr = list(map(int, input().split()))
print(twoSumTrouble(n, s, arr))