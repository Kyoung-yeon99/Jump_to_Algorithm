from collections import deque
def bfs(x, y, color, visited):
    qu = deque()
    qu.append((x, y))
    visited[x][y] = 1

    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if m[nx][ny] in color and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    qu.append((nx, ny))


n = int(input())
m = [list(map(str, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for color in ('R', 'G', 'B', ['R', 'G'], 'B'):
    visited = [[0]*n for _ in range(n)]
    if type(color) == list:
        print(cnt, end=' ')
        cnt = 0
    for i in range(n):
        for j in range(n):
            if m[i][j] in color and visited[i][j] == 0:
                bfs(i, j, color, visited)
                cnt += 1
print(cnt)
"""
rgb_cnt = 0
for color in ('R', 'G', 'B'):
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if m[i][j] == color and visited[i][j] == 0:
                bfs(i, j, color, visited)
                rgb_cnt += 1


rb_cnt = 0
for color in (['R', 'G'], 'B'):
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if m[i][j] in color and visited[i][j] == 0:
                bfs(i, j, color, visited)
                rb_cnt += 1

print(rgb_cnt, rb_cnt)
"""
