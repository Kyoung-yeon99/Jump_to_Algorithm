n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

'''
# 증가하면 dp[i-1] + 1
# 연속 아니면 dp[i] = dp[i-1]

# 마지막으로 증가한 수 저장
# temp = nums[0]
temp = 0
for i in range(1, n):
    if temp < nums[i]:
        dp[i] = dp[i-1] + 1
        temp = nums[i]
    else:
        dp[i] = dp[i-1]

print(dp[-1])

# 10 50 10 20 30 40 
# -> 10 50 만 보고 2라고 나옴 
# -> 10 20 30 40 여서 4임

'''