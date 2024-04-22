n = int(input())

# dp[i][j]: 길이가 i 인 계단 수가 j로 끝나는 개수
# j의 양 끝에 패딩 추가
dp = [[0 for _ in range(12)] for _ in range(n)]

# 초기화
dp[0] = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

# 점화식 - dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
for i in range(1, n):
    for j in range(1, 11):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n-1]) % 1000000000)