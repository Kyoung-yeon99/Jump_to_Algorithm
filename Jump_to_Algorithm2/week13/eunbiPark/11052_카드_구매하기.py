n = int(input())
costs = list(map(int, input().split()))
costs.insert(0, 0)

# dp[i] : 카드 i 개를 구매했을 때 금액의 최댓값
dp = [0 for _ in range(n + 1)]

# 점화식
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], costs[j] + dp[i-j])

print(dp[n])