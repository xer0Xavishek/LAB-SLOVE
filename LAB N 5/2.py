import sys
sys.setrecursionlimit(2 * 10**5 + 5)

def main():
    n, m = map(int, sys.stdin.readline().split())
    u = list(map(int, sys.stdin.readline().split()))
    v = list(map(int, sys.stdin.readline().split()))
    
    adj = [[] for _ in range(n + 1)]
    for i in range(m-1, -1, -1):
        a = u[i]
        b = v[i]
        adj[a].append(b)
        adj[b].append(a)
    
    visited = [False] * (n + 1)
    result = []
    
    def dfs(node):
        visited[node] = True
        result.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(1)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()