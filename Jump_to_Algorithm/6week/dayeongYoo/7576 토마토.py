from collections import deque

# 가로, 세로
m, n = map(int, input().split())
# 인접행렬
board = [list(map(int, input().split())) for _ in range(n)]
# 최소 날짜
ans = 0
# 길찾기-dx dy
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

q = deque()

# 인접행렬 채우기
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j, 0))


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


while q:
    x, y, d = q.popleft() # xy위치, 날짜
    ans = max(ans, d)

    nd = d + 1 # new day 갱신

    for k in range(4): # 사방탐경
        nx = x + dx[k]
        ny = y + dy[k]
        if in_range(nx, ny) and board[nx][ny] == 0:
            board[nx][ny] = 1
            q.append((nx, ny, nd))

for row in board:
    if 0 in row:  # bfs 후에도 0이 있다면
        ans = -1 # 토마토가 익지 못하는 상태임
        break

print(ans)
