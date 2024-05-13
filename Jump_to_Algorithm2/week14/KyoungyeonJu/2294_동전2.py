import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins = list(set(coins))   # 가치가 같은 동전 여러 번 주어질 수도 있기 때문에
dp = [int(1e5)] * (k+1)  # 1≤ k ≤ 10000
dp[0] = 0

for coin in coins:
    if coin > k:  # 동전 가치는 100,000보다 작거나 같은 자연수
        continue
    dp[coin] = 1
    for i in range(coin+1, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[-1]) if dp[-1] != int(1e6) else print(-1)
