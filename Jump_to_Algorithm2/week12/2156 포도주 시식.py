N = int(input())
wines = [0] + [int(input()) for _ in range(N)] + [0]

dp = [0] * (N + 2)

# 1, 2일 경우 최댓값은 연속으로 마신 경우임(초기값 지정)
dp[1] = wines[1]
dp[2] = dp[1] + wines[2]

# dp 갱신
for i in range(3, N + 1):
    dp[i] = max(dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i], dp[i - 1])
print(dp[N])
