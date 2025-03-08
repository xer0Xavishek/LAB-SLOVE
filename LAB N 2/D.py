def binaryString(s):
    l, r = 0, len(s) - 1
    result = -1

    while l <= r:
        mid = (l + r) // 2
        if s[mid] == '1':
            result = mid + 1  # Use 1-based index
            r = mid - 1
        else:
            l = mid + 1

    return result

t = int(input())

for k in range(t):
    s = input()
    print(binaryString(s))

# 0 based index
def binaryString(s):
    l, r = 0, len(s) - 1
    result = -1

    while l <= r:
        mid = (l + r) // 2
        if s[mid] == '1':
            result = mid  # Use 0-based index
            r = mid - 1
        else:
            l = mid + 1

    return result

t = int(input())

for k in range(t):
    s = input()
    print(binaryString(s))