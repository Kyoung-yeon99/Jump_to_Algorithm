# 맨 위층에서부터 대각선 왼쪽 또는 대각선 오른쪽을 선택하여 아래층으로 내려올 때 선택된 수의 합의 최댓값
import sys

input = sys.stdin.readline
n = int(input()) # 삼각형의 크기
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n): # 각 행에 대해
    for j in range(i+1): # 각 숫자를 선택했을 때
        if j == 0: # 첫번째 숫자라면
            dp[i][j] += dp[i-1][j]
        elif j == i: # 마지막 숫자라면
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))


# 시간 초과
# import sys

# input = sys.stdin.readline
# n = int(input()) # 삼각형의 크기
# t = [[] for _ in range(n)]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     t[i] = list(map(int, input().split()))

# dp[0][0] = t[0][0]

# def go_down(r, c):
#     if r == n-1: # 맨 아래층일 경우 종료
#         return
    
#     dl = dp[r][c] + t[r+1][c] # 대각선 왼쪽
#     if dp[r+1][c] < dl:
#         dp[r+1][c] = dl
#         go_down(r+1, c)

#     dr = dp[r][c] + t[r+1][c+1] # 대각선 오른쪽
#     if dp[r+1][c+1] < dr:
#         dp[r+1][c+1] = dr
#         go_down(r+1, c+1)

# go_down(0, 0)
# print(max(dp[n-1]))