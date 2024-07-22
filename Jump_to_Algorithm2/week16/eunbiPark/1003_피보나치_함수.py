t = int(input())

# dp[i][0]: fibo(i)을 호출 했을 때 0 출력 횟수
# dp[i][1]: fibo(i)을 호출 했을 때 1 출력 횟수
dp = [[0, 0] for _ in range(41)]

# 초기화
dp[0][0] = 1
dp[1][1] = 1

# 점화식
for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for _ in range(t):
    num = int(input())
    print(*dp[num])