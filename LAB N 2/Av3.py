def twoSumTrouble(n, s, arr):
    idx_arr = [(value, index ) for index, value in enumerate(arr)]
    

    l, r = 0, n - 1
    while l < r:
        current_sum = idx_arr[l][0] + idx_arr[r][0] # sum of the two elements at the current indices l and r korte korte
        
        if current_sum == s:
            return f"{idx_arr[l][1] + 1} {idx_arr[r][1] + 1}"  # 1-indexed
        
        elif current_sum < s: # if the sum is less than s, then we need to increase the sum, so we increase the left index

            l += 1 # increasing the left index will increase the sum

        else: # if the sum is greater than s, then we need to decrease the sum, so we decrease the right index

            r -= 1 # decreasing the right index will decrease the sum

    return -1   # if no such pair exists, return -1

n, s = map(int, input().split())
arr = list(map(int, input().split()))
print(twoSumTrouble(n, s, arr))