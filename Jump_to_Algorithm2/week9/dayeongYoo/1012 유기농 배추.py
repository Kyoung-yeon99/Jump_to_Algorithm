# https://dduniverse.tistory.com/entry/백준-1012-유기농-배추-파이썬-python

import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[ny][nx] == 1:
            board[ny][nx] = 0  # 배추 방문 처리
            dfs(nx, ny)


# 테케
t = int(input())
for _ in range(t):
    # 가로, 세로, 배추 개수
    m, n, k = map(int, input().split())
    # 배추 위치 맵
    board = [[0 for _ in range(m)] for _ in range(n)]

    # 배추 위치 표시
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1  # 행,열 순으로 접근

    # 배추 덩어리(그룹)
    cnt = 0
    for i in range(m):
        for j in range(n):
            if board[j][i] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
