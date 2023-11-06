n = int(input())
seq = list(map(int, input().split()))

dp = [1 for _ in range(n)] # i번째까지의 수열에서 가장 긴 증가하는 수열의 길이
for i in range(1, n): 
    for j in range(i-1, -1, -1):
        if seq[i] > seq[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
print(max(dp))