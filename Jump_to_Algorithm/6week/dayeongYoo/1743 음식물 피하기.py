import sys

sys.setrecursionlimit(10 ** 8)

n, m, k = map(int, input().split())
board = [['.'] * m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = '#'
visited = [[False] * m for _ in range(n)]

food_size = 0  # 음식물 크기
ans = 0  # 답

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


# 범위체크
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(x, y):
    global ans, food_size
    visited[x][y] = True
    food_size = 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == '#':
            food_size += dfs(nx, ny)

    ans = max(ans, food_size)
    return food_size


# dfs
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == '#':
            dfs(i, j)
print(ans)
