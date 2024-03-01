# 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것
s1 = input()
s2 = input()
dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
lcs = 0

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            lcs = max(lcs, dp[i+1][j+1])
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
      
print(lcs)


# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence