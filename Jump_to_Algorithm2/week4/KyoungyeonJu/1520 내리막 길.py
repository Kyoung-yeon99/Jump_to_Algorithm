import sys
input = sys. stdin.readline

# matrix[x][y]에서 도착 지점까지 갈 수 있는 경우의 수 구해서 dp[x][y] 값 갱신하기
def path(x, y):
    if x == m-1 and y == n-1:  # 도착지점에 도착하면 1 return
        return 1

    if dp[x][y] != -1:  # 이미 dp 테이블 값이 갱신된 위치이면 해당 위치의 값 return
        return dp[x][y]

    a = 0  # 갱신되지 않은 위치이면
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:  # 범위 안에 있는 좌표
            if matrix[nx][ny] < matrix[x][y]:  # 이전 값보다 작고
                a += path(nx, ny)  # 해당 위치에서 도착위치까지 갈 수 있는 경우의 수 업데이트

    dp[x][y] = a  # 좌표(x, y)에서 도착 지점까지 갈 수 있는 경우의 수 구해서 dp 테이블 갱신
    return dp[x][y]


m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]  # 상하좌우

dp = [[-1]*n for _ in range(m)]

print(path(0, 0))


""" 
# 시간초과 dp 사용안함..
import sys
input = sys.stdin.readline

def path(x, y):
    global cnt

    if x == m-1 and y == n-1:
        cnt += 1
        return

    std = matrix[x][y]  # 기준값

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:  # 범위 안에 있는 좌표
            if matrix[nx][ny] < std:  # 기준값보다 작고
                path(nx, ny)


m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]  # 상하좌우
cnt = 0
path(0, 0)
print(cnt)
"""