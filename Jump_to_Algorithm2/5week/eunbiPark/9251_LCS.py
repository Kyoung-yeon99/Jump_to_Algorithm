# 두 수열 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾기

import sys
input = sys.stdin.readline

str1 = input().strip().upper()
str2 = input().strip().upper()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]: # 같은 글자가 등장했다면
            dp[i][j] = dp[i-1][j-1] + 1 # 이전 값 보다 하나 커짐
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])