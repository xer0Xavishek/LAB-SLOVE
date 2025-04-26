def main():
    N = int(input())
    x1, y1, x2, y2 = map(int, input().split())
    
    dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]
    
    dis = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
    dis[x1][y1] = 0  
    Q = []
    Q.append((x1, y1))
    
    while Q:
        x, y = Q.pop(0)
        if x == x2 and y == y2:
            print(dis[x][y])
            return
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= N and 1 <= ny <= N and dis[nx][ny] == -1:
                dis[nx][ny] = dis[x][y] + 1
                Q.append((nx, ny))
    
    print(-1)

if __name__ == "__main__":
    main()