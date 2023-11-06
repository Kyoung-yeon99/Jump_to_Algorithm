n = int(input())
t, p = [0] * n, [0] * n
for i in range(n):
    t[i], p[i] = map(int, input().split())

dp = [0 for _ in range(n)]

for i in range(n):
    if t[i] <= n-i and dp[i] < p[i]: # i번째 날 상담이 가능하고 현재 dp[i] 값보다 p[i]가 클 경우 dp[i]에 저장
        dp[i] = p[i]
    for j in range(i+t[i], n): # i번째 날 상담을 하고 j번째 날 상담을 할 경우
        if dp[j] < dp[i] + p[j] and j <= n - t[j]: # 현재 dp[j]보다 이익이 클 경우 dp[j] 갱신
            dp[j] = dp[i] + p[j]

print(max(dp))

# dp = [0 for _ in range(n+1)]
# # i번째까지 일했을 때 얻는 최대 수익 계산
# for i in range(n):
#     for j in range(i+t[i], n+1): # i번째 날에 상담을 했을 때 마지막 날까지 상담이 가능한 날짜
#         if dp[j] < dp[i] + p[i]:
#             dp[j] = dp[i] + p[i] # 상담을 했을 때 얻는 최대 수익
# print(dp[-1])
