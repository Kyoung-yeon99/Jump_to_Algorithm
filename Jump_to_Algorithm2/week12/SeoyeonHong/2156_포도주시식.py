# 최대로 마실 수 있는 포도주의 양
import sys

input = sys.stdin.readline
n = int(input()) # 포도주 잔의 개수
wine = []
for _ in range(n):
    wine.append(int(input()))

# 연속으로 놓여 있는 3잔을 모두 마실 수는 없음
dp = [[0 for _ in range(3)] for _ in range(n)]

dp[0][1] = wine[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + wine[i]
    dp[i][2] = dp[i-1][1] + wine[i]

print(max(dp[n-1]))
