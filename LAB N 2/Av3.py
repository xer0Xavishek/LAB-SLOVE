def twoSumTrouble(n, s, arr):
    idx_arr = [(value, index ) for index, value in enumerate(arr)]
    

    l, r = 0, n - 1
    while l < r:
        current_sum = idx_arr[l][0] + idx_arr[r][0]
        if current_sum == s:
            return f"{idx_arr[l][1] + 1} {idx_arr[r][1] + 1}"
        elif current_sum < s:
            l += 1
        else:
            r -= 1
    return -1

n, s = map(int, input().split())
arr = list(map(int, input().split()))
print(twoSumTrouble(n, s, arr))