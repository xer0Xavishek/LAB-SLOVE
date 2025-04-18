
R, C = map(int, input().split())


grid = [input().strip() for l in range(R)]


vstd = [[False] * C for k in range(R)]


dirs = [(1,0),(-1,0),(0,1),(0,-1)]

mxD = 0

for i in range(R):


    for j in range(C):


        if grid[i][j] != '#' and not vstd[i][j]:

            Q = [(i, j)]

            vstd[i][j] = True

            head = 0

            cnt = 0

            while head < len(Q):

                x, y = Q[head]

                head += 1

                if grid[x][y] == 'D':

                    cnt += 1

                for dx, dy in dirs:

                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < R and 0 <= ny < C \
                        and not vstd[nx][ny] \
                        and grid[nx][ny] != '#':
                        vstd[nx][ny] = True
                        Q.append((nx, ny))

            if cnt > mxD:
                mxD = cnt

print(mxD)


