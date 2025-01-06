# 0은 갈 수 없는 땅, 1은 갈 수 있는 땅, 2는 목표지점
# 입력에서 2는 단 한 개
# 각 지점에서 목표지점까지의 거리 출력
# 원래 갈 수 없는 땅은 0, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1 출력

# bfs -> deque
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    global ans, maps
    visited[x][y] = True
    ans[x][y] = 0
    q = deque()
    q.append((x, y))

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dx[i], c+dy[i]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and maps[nr][nc] == 1:
                    ans[nr][nc] = ans[r][c]+1
                    visited[nr][nc] = True
                    q.append((nr, nc))


n, m = map(int, input().split())  # 2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000
visited = [[False]*m for _ in range(n)]
ans = [[0]*m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
maps = []
start_x, start_y = -1, -1
for i in range(n):
    row = list(map(int, input().split()))
    if 2 in row:
        start_x = i
        start_y = row.index(2)
    maps.append(row)

bfs(start_x, start_y)

for i in range(n):
    for j in range(m):
        # -1의 조건은 not visited이면서 maps[i][j]==1인 경우
        if maps[i][j] == 1 and not visited[i][j]:
            ans[i][j] = -1

for i in range(n):
    print(*ans[i])
