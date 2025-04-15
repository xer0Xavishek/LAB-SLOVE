def bubbleSort(size, arr):
    for i in range(size - 1):
        flag = False
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break

size = int(input())
x = [int(i) for i in input().split()]

bubbleSort(size, x)
print(' '.join(str(i) for i in x))