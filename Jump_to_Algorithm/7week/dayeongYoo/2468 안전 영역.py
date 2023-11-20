import sys

sys.setrecursionlimit(10 ** 8)

# 크기
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 안전영역
ans = 1

# dxs dys
dxs = (-1, 0, 1, 0)
dys = (0, 1, 0, -1)


def dfs(x, y, h):  # 현재 좌표, 높이
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        # 범위 안에 있는지, 방문하지 않았고, 물에 잠기는 높이보다 클때(안전영역)
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] > h:
            visited[nx][ny] = True  # 방문처리
            dfs(nx, ny, h)


# 시뮬레이션
for max_h in range(max(map(max, board))):  # 2차원이므로 전체 max를 구하기 위해서 1. board 행에서 최댓값을 구한다음, 2. 그 중 최대값 구함.

    # 방문 체크
    visited = [[False] * n for _ in range(n)]

    safe = 0  # 안전영역
    for i in range(n):
        for j in range(n):
            if board[i][j] > max_h and not visited[i][j]:  # 최댓값 보다 크고, 방문하지 않았다면
                safe += 1  # 안전영역 1 증가
                visited[i][j] = True  # 방문처리
                dfs(i, j, max_h)
    ans = max(ans, safe)  # 최댓값
print(ans)
