n = int(input())
times = list(map(int, input().split()))
times.append(0)
times.sort()

# dp[i]: i 번째 time 까지 대기 시간
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = dp[i-1] + times[i]

print(sum(dp))