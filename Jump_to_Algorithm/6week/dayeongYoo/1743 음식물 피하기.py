import sys

sys.setrecursionlimit(10 ** 8)

# 세로, 가로, 음식물 개수
n, m, k = map(int, input().split())
# graph -> 인접행렬
board = [['.'] * m for _ in range(n)]
# 음식물 좌표 체크
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = '#'  # 1-based -> 0-based(-1 해준다)
# 방문 체크
visited = [[False] * m for _ in range(n)]

food_size = 0  # 음식물 크기
ans = 0  # 답

# 길찾기 dx, dy
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


# 범위체크
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(x, y):
    global ans, food_size
    visited[x][y] = True  # 방문 체크
    food_size = 1  # 음식물 크기 초기화

    for k in range(4):  # 4방 탐색
        nx = x + dx[k]
        ny = y + dy[k]
        # 범위 내, 방문 x, 음식물이 있는 위치라면
        if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == '#':
            # 인접한 음식물 크기 합치기
            food_size += dfs(nx, ny)
            # 제일 큰 음식물 크기
    ans = max(ans, food_size)
    return food_size


# dfs
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == '#':
            dfs(i, j)
print(ans)
