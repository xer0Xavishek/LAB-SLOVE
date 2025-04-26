import sys


sys.setrecursionlimit(2 * 10**5 + 5)

class vertex:
    
    def __init__(self, ip):

        self.val = ip

        self.col = "WHITE"

        self.adj_li = []

def depthfirst(start):

    start.col = "GRAY"

    print( start.val, end=" " )

    for n in start.adj_li:

        if n.col == "WHITE":

            depthfirst(n)


    start.col = "BLACK"

def solv():

    s, t = map( int, input().split()  )

    a = input().split(" ")

    b = input().split(" ")

    lst = [None]*(s+1)

    for i in range(t):

        u = int(a[i])
        v = int(b[i])

        if lst[u] == None:

            lst[u] = vertex(u)

        if lst[v] == None:

            lst[v] = vertex(v)

        lst[u].adj_li.append(lst[v])

        lst[v].adj_li.append(lst[u])

    depthfirst(lst[1])


if __name__ == "__main__":
    solv()