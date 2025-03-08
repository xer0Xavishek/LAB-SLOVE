import sys

def low(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

def high(arr, y):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= y:
            l = mid + 1
        else:
            r = mid
    return l

n, q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

results = []
for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    lower = low(arr, x)
    upper = high(arr, y)
    results.append(str(upper - lower))

sys.stdout.write("\n".join(results) + "\n")
