# 0: 이동 가능, 1: 이동 불가
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

walls = [
    (i, j)
    for i in range(n)
    for j in range(m)
    if board[i][j]
]

walls.insert(0, (0, 0))

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
         return False
    return True

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not temp[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    dist = visited[n-1][m-1]
    if not dist:
        return float('inf')
    else:
        return dist

ans = float('inf')
# main
# 1. 부술 벽 선택
for w in walls:
    # 2. 최단거리 계산
    # 2-1. board 복제
    temp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = board[i][j]

    # 2-2. 벽 부수기
    temp[w[0]][w[1]] = 0

    # 2-3. 최단 거리 구하기
    q = deque()
    q.append((0, 0))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1

    ans = min(ans, bfs())

print(-1) if ans == float('inf') else print(ans)

# 반례 모음
# https://www.acmicpc.net/board/view/119335

