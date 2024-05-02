n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp[i]: i원을 만들 수 있는 동전의 최소 개수
dp = [float('inf')] * (k + 1) # min 값 비교할 거라 최댓값으로 초기화

# 초기화
for c in coins:
    if c <= k: # 만들 수 보다 큰 가치의 동전이 들어올 수 있음
        dp[c] = 1 # 해당 동전 하나만 사용해서 그 숫자를 만들 수 있다

# 점화식
for i in range(1, k + 1):
    for c in coins:
        if i - c > 0: # c를 활용해서 수를 만들 수 있으면
            dp[i] = min(dp[i-c] + 1, dp[i])

print(-1) if dp[k] == float('inf') else print(dp[k])