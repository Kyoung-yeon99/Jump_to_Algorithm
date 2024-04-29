# 인접한 모든 자리의 차이가 1인수: 계단수
# 0으로 시작하는 수는 계단 수 아님
# 1,000,000,000으로 나눈 나머지 출력

# https://velog.io/@iamjinseo/백준10844-쉬운-계단-수

n = int(input())
# 이중 리스트
dp = [[0] * 10 for _ in range(n + 1)]

# 자릿수가 하나일 때 삽입
for i in range(1, 10):
    dp[1][i] = 1

# 자릿수에 따라, 0~9 까지 수가 맨 뒤에 올 수 있는 경우의 수
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

# 1,000,000,000으로 나눈 나머지를 출력
print(sum(dp[n]) % 1000000000)
