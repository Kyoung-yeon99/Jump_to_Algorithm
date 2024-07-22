# 합이 n과 같게 되는 제곱수들의 최소 개수
# 시간 초과
import math

n = int(input())
square = math.sqrt(n)

if square % 1 == 0 : # 제곱수일 경우
    print(1)
else:
    square = int(square)
    dp = [i for i in range(n+1)] # dp[i] == 합이 i와 같게 되는 제곱수들의 최소 개수
    for i in range(1, square+1): 
        dp[pow(i, 2)] = 1 # 제곱수의 경우 1

    m = 0
    for i in range(1, n+1):
        if dp[i] != i: # 4 이상의 제곱수일 경우
            m = pow(int(math.sqrt(i)) - 1, 2)
        else:
            for j in range(m, i):
                dp[i] = min(dp[i], dp[j] + dp[i-j])
    print(dp[n])