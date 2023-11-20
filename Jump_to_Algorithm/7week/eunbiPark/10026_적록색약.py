import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
grid = [
    list(sys.stdin.readline().rstrip())
    for _ in range(n)
]
visited = [
    [False] * n
    for _ in range(n)
]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    visited[y][x] = True
    color = grid[y][x]
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[ny][nx] == False and grid[ny][nx] == color:
                dfs(nx, ny)

cnt, cnt2 = 0, 0

for y in range(n):
    for x in range(n):
        if visited[y][x] == False:
            dfs(x, y)
            cnt += 1

for y in range(n):
    for x in range(n):
        if grid[y][x] == 'G':
            grid[y][x] = 'R'
visited = [
    [False] * n
    for _ in range(n)
]

for y in range(n):
    for x in range(n):
        if visited[y][x] == False:
            dfs(x, y)
            cnt2 += 1

print(cnt, cnt2)