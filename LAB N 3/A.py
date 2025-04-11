def merge(a, b):

    merged = []
    i = j = 0

    while i < len(a) and j < len(b):

        if a[i] <= b[j]:

            merged.append(a[i])
            i += 1

        else:

            merged.append(b[j])
            j += 1
            global invrsns
            invrsns += len(a) - i  

    merged+=a[i:]

    merged+=b[j:]

    return merged


def mergeSort(arr):

    if len(arr) <= 1:

        return arr
    else:

        m = len(arr) // 2

        l = mergeSort(arr[:m])

        r = mergeSort(arr[m:])
        
        return merge(l, r)




n = int(input())


arr = list(map(int, input().split()))

invrsns = 0

srtd = mergeSort(arr)

print(invrsns)

print(" ".join(map(str, srtd)))