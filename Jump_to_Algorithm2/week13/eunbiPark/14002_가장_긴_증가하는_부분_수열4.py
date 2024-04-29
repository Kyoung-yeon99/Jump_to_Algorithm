n = int(input())
nums = list(map(int, input().split()))

# dp[i]: i번재 수를 선택할 때 부분수열의 최대 길이
dp = [1] * n

# 점화식
for i in range(n):
    mx = 0
    for j in range(i):
        if nums[i] > nums[j]:
            mx = max(mx, dp[j])
    dp[i] = mx + 1

mx = max(dp)
print(mx)
route = []
for i in range(n-1, -1, -1):
    if dp[i] == mx:
        route.append(nums[i])
        mx -= 1

route.reverse()
print(*route)