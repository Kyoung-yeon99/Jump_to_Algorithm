k = int(input())

a_dp = [0] * (k + 1)
b_dp = [0] * (k + 1)

# a_dp[1] = 1, b_dp[1] = 0
# a_dp[2] = 0 b_dp[2] = 1
# a_dp[3] = 1 b_dp[3] = 1
# a_dp[4] = 1 b_dp[4] = 2
# a_dp[i] = b_dp[i-1]
# b_dp[i] = a_dp[i-1] + b_dp[i-1]

a_dp[1] = 0
b_dp[1] = 1

for i in range(2, k + 1):
    a_dp[i] = b_dp[i-1]
    b_dp[i] = a_dp[i-1] + b_dp[i-1]

print(a_dp[-1], b_dp[-1])