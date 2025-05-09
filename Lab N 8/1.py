import sys
from sys import stdin

def main():
    sys.setrecursionlimit(1 << 25)
    N, K = map(int, stdin.readline().split())
    par = [i for i in range(N + 1)]
    s = [1] * (N + 1)

    def find(u):
        while par[u] != u:
            par[u] = par[par[u]]
            u = par[u]
        return u

    def union(u, v):
        urt = find(u)
        vrt = find(v)
        if urt == vrt:
            return s[urt]
        if s[urt] < s[vrt]:
            par[urt] = vrt
            s[vrt] += s[urt]
            return s[vrt]
        else:
            par[vrt] = urt
            s[urt] += s[vrt]
            return s[urt]

    for p in range(K):
        a, b = map(int, stdin.readline().split())
        res = union(a, b)
        print(res)

if __name__ == "__main__":
    main()