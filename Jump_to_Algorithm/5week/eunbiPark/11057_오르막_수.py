# 모든 수를 보고 판단하는 것 x, 점화식 세우기

n = int(input())

# 끝 자릿수
dp = [1] * 10

# 자릿수 만큼 반복
for i in range(n-1):
    # 끝 자릿수 반복
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp) % 10007)