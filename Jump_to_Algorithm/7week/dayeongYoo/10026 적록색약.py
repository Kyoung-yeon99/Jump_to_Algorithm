import sys

sys.setrecursionlimit(10 ** 8) # dfs

n = int(input())
board = [input() for _ in range(n)]

# 4방탐색
dxs = (-1, 0, 1, 0)
dys = (0, 1, 0, -1)


# 범위 체크
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# dfs
def dfs(x, y, color):
    for k in range(4):
        nx, ny = x + dxs[k], y + dys[k]
        if in_range(nx, ny) and board[nx][ny] in color and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, color)


# 구역 개수
ans = 0
# 방문체크
visited = [[False] * n for _ in range(n)]
# 1. 적록색약이 아닌 사람
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans += 1
            visited[i][j] = True
            dfs(i, j, board[i][j])
print(ans, end=' ')

# 2. 적록색약인 사람
ans = 0
# 방문체크
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans += 1
            visited[i][j] = True
            dfs(i, j, 'B' if board[i][j] == 'B' else 'RG')  # B라면 그대로 영역 개수를 세고, b와 다르다면 즉, 적록 중 하나라면 R, G를 동일화한다.

print(ans)
