  # 10^7

def fastmDrift(a,b):

    m = 107
    res = 1

    while b>0:

        if b%2==1:
            res = (res*a) % m
        a = (a * a) % m
        b= b // 2
    return res


a, b = map(int, input().split())


print(fastmDrift(a, b))
