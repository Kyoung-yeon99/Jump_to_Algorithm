n = int(input())
nums = [int(input()) for _ in range(n)]
nums.append(0)
# dp[i][0]: i 번째 포도주를 먹는데 연속으로 0잔 먹기
# dp[i][1]: i 번째 포도주를 먹는데 연속으로 1잔 먹기
# dp[i][2]: i 번째 포도주를 먹는데 연속으로 2잔 먹기
dp = [[0, 0, 0] for _ in range(10005)]

# 초기화
dp[1] = [0, nums[0], 0]

# 점화식
mx = -float('inf')
for i in range(2, n + 1):
    dp[i][0] = max(dp[i-1][0],dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + nums[i-1]
    dp[i][2] = dp[i-1][1] + nums[i-1]
    mx = max(mx, dp[i][0], dp[i][1], dp[i][2])

print(sum(nums)) if mx == -float('inf') else print(mx)