# 직사각형 지도
# 한 칸: 한 지점을 나타냄.
# 각 칸에는 그 지점의 높이가 쓰여짐.
# 각 지점 사이 이동: 상하좌우만 가능.

# 제일 왼쪽 위 칸 -> 제일 오른쪽 아래 칸으로
# 가능한 힘을 적게 들여 "항상 높이가 낮은 지점"(최솟값)으로 이동

# 경로의 개수 출력
# 최단거리인데, 모든 경로를 모두 탐색해야 하므로 dfs.
# https://www.acmicpc.net/problem/1520

import sys

sys.setrecursionlimit(10 ** 6)

# 세로(x), 가로(y)
m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(m)]

# 북-동-남-서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 최솟값을 갱신하기 위한 dp 테이블(cache용)
cache = [[-1] * n for _ in range(m)]


# 범위 안 체크
def in_range(x, y):
    return 0 <= x < m and 0 <= y < n


def dfs(x, y):
    # 재귀 탈출 조건
    if x == (m - 1) and y == (n - 1):
        return 1  # 도착 지점 도착시 경우의 수 +1
    # 방문했다면 그 위치에서 출발하는 경우의 수 리턴<--핵심 코드
    if cache[x][y] != -1:
        return cache[x][y]
    # 정답
    ans = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):  # 가지치기
            continue
        if board[x][y] > board[nx][ny]:  # 낮은 높이의 셀로 이동
            # 또 다른 경로를 가려면?
            ans += dfs(nx, ny)
    cache[x][y] = ans
    return cache[x][y]


print(dfs(0, 0))
