import sys
from sys import stdin

def main():

    sys.setrecursionlimit(1 << 25)

    N, M = map(int, stdin.readline().split())

    edges = []

    for k in range(M):


        u, v, w = map(int, stdin.readline().split())

        edges.append((w, u, v))
    
    edges.sort()

    par = [i for i in range(N + 1)]


    size = [1] * (N + 1)

    def find(u):


        while par[u] != u:


            par[u] = par[par[u]]

            u = par[u]
        return u

    tcst = 0

    for w, u, v in edges:

        urt = find(u)

        vrt = find(v)

        if urt != vrt:

            tcst += w

            if size[urt] < size[vrt]:

                par[urt] = vrt

                size[vrt] += size[urt]

            else:

                par[vrt] = urt

                size[urt] += size[vrt]

    
    print(tcst)

if __name__ == "__main__":
    
    main()