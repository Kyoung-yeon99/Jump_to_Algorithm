n = int(input())
t, p = [0] * n, [0] * n
for i in range(n):
    t[i], p[i] = map(int, input().split())

dp = [0 for _ in range(n+1)]

# i번째까지 일했을 때 얻는 최대 수익 계산
for i in range(n):
    for j in range(i+t[i], n+1): # i번째 날에 상담을 했을 때 마지막 날까지 상담이 가능한 날짜
        if dp[j] < dp[i] + p[i]:
            dp[j] = dp[i] + p[i] # 상담을 했을 때 얻는 최대 수익

print(dp[-1])
