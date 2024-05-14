import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for i in range(n)]

# dp[i][j][k]: (i, j) 위치 집에 k 파이프 모양이 가능한 경우의 수
result = [[[0 for i in range(n)] for i in range(n)] for i in range(3)]

# 초기화
result[0][0][1] = 1
for i in range(2, n):
    if s[0][i] == 0:
        result[0][0][i] = result[0][0][i - 1]

# 점화식
for i in range(1, n):
    for j in range(2, n):
        # 대각선 파이프 추가
        if s[i][j] == 0 and s[i - 1][j] == 0 and s[i][j - 1] == 0:
            result[2][i][j] = result[0][i - 1][j - 1] + result[1][i - 1][j - 1] + result[2][i - 1][j - 1]

        # 가로, 세로 파이프 추가
        if s[i][j] == 0:
            result[0][i][j] = result[0][i][j - 1] + result[2][i][j - 1]
            result[1][i][j] = result[1][i - 1][j] + result[2][i - 1][j]

print(result[0][n - 1][n - 1] + result[1][n - 1][n - 1] + result[2][n - 1][n - 1])