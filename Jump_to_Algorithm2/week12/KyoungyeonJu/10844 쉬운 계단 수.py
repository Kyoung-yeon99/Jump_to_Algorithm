n = int(input())
dp = [[0]*10 for _ in range(n+1)]
num = 1000000000
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, n+1):
    dp[i][0] = dp[i-1][1] % num
    for j in range(1, 9):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1]) % num
    dp[i][9] = dp[i-1][8] % num

print(sum[dp[n]] % num)
