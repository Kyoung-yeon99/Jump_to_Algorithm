tc = int(input())
t = [int(input()) for _ in range(tc)]
dp = [[1, 0], [0, 1]]

for i in range(2, 41):
    num_0 = dp[i-1][0] + dp[i-2][0]
    num_1 = dp[i-1][1] + dp[i-2][1]
    dp.append([num_0, num_1])

for i in t:
    print(*dp[i])
