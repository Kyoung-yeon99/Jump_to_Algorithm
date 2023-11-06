n = int(input())
times = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [0] * (n + 1)

# top-down

for i in range(n-1, -1, -1):
    # 퇴사일 넘기는 지 확인 
    if i + times[i][0] > n:
        dp[i] = dp[i+1]
    else:
        # 상담을 하는 것과 하지 않는 것 중 큰 것 선택
        dp[i] = max(dp[i+1], times[i][1] + dp[i + times[i][0]])

print(dp[0])

'''
# bottom-up

for i in range(n):
    for j in range(i + times[i][0], n + 1):
        # 갱신이 안되었다면 
        if dp[j] < dp[i] + times[i][1]:
            dp[j] = dp[i] + times[i][1]

print(dp[-1])

'''