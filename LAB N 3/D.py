def fast_exponentiation(a, b, mod):
    result = 1
    a = a % mod
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b = b // 2
    return result

def geometric_series_sum(a, n, m):
    if a == 1:
        return n % m
    mod = m * (a - 1)
    a_n_plus_1 = fast_exponentiation(a, n + 1, mod)
    numerator = (a_n_plus_1 - a) % mod
    sum_mod = numerator // (a - 1)
    return sum_mod % m

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        a = int(data[index])
        n = int(data[index + 1])
        m = int(data[index + 2])
        index += 3
        result = geometric_series_sum(a, n, m)
        results.append(result)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()