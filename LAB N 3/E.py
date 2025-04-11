def mx_6ft(arr, start, end, res):

    if start > end:

        return
    
    m = (start + end) // 2

    res.append(arr[m])
    
    mx_6ft(arr, start, m - 1, res)

    mx_6ft(arr, m + 1, end, res)

def main():

    N = int(input())

    arr = list(map(int, input().split()))
    
    res = []
    
    mx_6ft(arr, 0, N - 1, res)
    
    print(" ".join(map(str, res)))

main()