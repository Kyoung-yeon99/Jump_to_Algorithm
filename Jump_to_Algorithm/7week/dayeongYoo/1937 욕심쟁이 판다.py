import sys

sys.setrecursionlimit(10 ** 8)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 4방탐색
dxs = (-1, 0, 1, 0)
dys = (0, 1, 0, -1)

# 이동 칸수
ans = 0


# 범위 체크
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# dfs
def dfs(x, y):  # 현재좌표
    if cache_route[x][y]:  # 이미 왔다가 경로는 계산하지 않는다.
        return cache_route[x][y]

    cache_route[x][y] = 1  # 초기화

    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if in_range(nx, ny) and board[nx][ny] > board[x][y]:
            # 이동 경로와 새로운 경로 길이(이동한 위치 +1)의 최대값
            cache_route[x][y] = max(cache_route[x][y], dfs(nx, ny) + 1)
    return cache_route[x][y]


# 이동칸
ans = 0
# 이동한 경로 저장용 cache
cache_route = [[0] * n for _ in range(n)]
# 실행
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)
