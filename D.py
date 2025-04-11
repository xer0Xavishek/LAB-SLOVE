def fstEx(a, b, mod):
    res = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            res= (res* a) % mod
        a = (a * a) % mod
        b = b // 2
    return res
def geoSum(a, n, m):
    if a == 1:
        return n % m
    mod = m * (a - 1)
    k_k = fstEx(a, n + 1, mod)
    num = (k_k - a) % mod
    smd = num // (a - 1)
    return smd % m

def main():
    import sys
    input = sys.stdin.read
    cline = input().split()
    T = int(cline[0])
    index = 1
    results = []
    for _ in range(T):
        a = int(cline[index])
        n = int(cline[index + 1])
        m = int(cline[index + 2])
        index += 3
        result = geoSum(a, n, m)
        results.append(result)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()