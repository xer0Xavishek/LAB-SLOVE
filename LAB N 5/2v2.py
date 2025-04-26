import sys
sys.setrecursionlimit(2 * 10**5 + 5)

class Node:
    def __init__(self, data):
        self.value = data
        self.color = "W"
        self.adj = []

def dfs(root):
    root.color = "G"
    print(root.value, end=" ")
    for neighbor in root.adj:
        if neighbor.color == "W":
            dfs(neighbor)
    root.color = "B"

def main():
    l, n = map(int, input().split())
    a = input().split(" ")
    b = input().split(" ")
    arr = [None] * (l + 1)

    for i in range(n):
        u = int(a[i])
        v = int(b[i])

        if arr[u] is None:
            arr[u] = Node(u)

        if arr[v] is None:
            arr[v] = Node(v)

        arr[u].adj.append(arr[v])
        arr[v].adj.append(arr[u])

    dfs(arr[1])

if __name__ == "__main__":
    main()