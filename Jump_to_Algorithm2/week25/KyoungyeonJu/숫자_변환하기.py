def solution(x, y, n):
    INF = int(1e6)
    dp = [INF]*(y+1)
    dp[x] = 0
    if x+n <= x*2:
        start = x+n
    else:
        start = x*2

    for i in range(start, y+1):
        if i % 6 == 0:
            dp[i] = min(dp[i], dp[i-n]+1, dp[i//2]+1, dp[i//3]+1)
        elif i % 3 == 0:
            dp[i] = min(dp[i], dp[i-n]+1, dp[i//3]+1)
        elif i % 2 == 0:
            dp[i] = min(dp[i], dp[i-n]+1, dp[i//2]+1)
        else:
            dp[i] = min(dp[i], dp[i-n]+1)

    return dp[-1] if dp[-1] != INF else -1