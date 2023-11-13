from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 최소 날짜
ans = 0
# dx dy
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j, 0))


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


while q:
    x, y, d = q.popleft()
    ans = max(ans, d)

    nd = d + 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if in_range(nx, ny) and board[nx][ny] == 0:
            board[nx][ny] = 1
            q.append((nx, ny, nd))

for row in board:
    if 0 in row:
        ans = -1
        break

print(ans)
