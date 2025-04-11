N = int(input())

x, y = map(int, input().split())

directions = [(0, 1),(0, -1),(-1, 0),(1, 0),(-1, 1),(1, 1),(-1, -1),(1, -1)]

res = []

for dx, dy in directions:

    a = x + dx

    b = y + dy

    if 1 <= a <= N and 1 <= b <= N:
        
        res.append((a, b))

res.sort()

print(len(res))

for m in res:

    print(m[0], m[1])