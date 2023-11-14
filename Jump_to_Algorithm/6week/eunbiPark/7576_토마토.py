from collections import deque
m, n = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

q = deque()

# 익은 토마토 촤표 저장
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append([i, j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append([nx, ny])

ret = 0
for b in board:
    for tomato in b:
        if tomato == 0:
            print(-1)
            exit()
    ret = max(ret, max(b))

print(ret - 1)