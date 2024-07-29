def solution(x, y, n):
    # 1. dp[i] : i를 만드는 데 드는 최소 연산 횟수
    dp = [float('inf')] * (y + 1)
    
    # 2. 초기화 
    dp[x] = 0
    
    # 3. 점화식 
    for i in range(x + 1, y + 1):
        if i - n != float('inf'):
            dp[i] = dp[i-n] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i//2] + 1, dp[i])
            # 이미 위에서 dp[i-n]일 때를 계산했으니 아래 식은 맞지 않음
            # dp[i] = min(dp[i//2], dp[i-n]) + 1
        if i % 3 == 0:
            dp[i] = min(dp[i//3] + 1, dp[i])
            # dp[i] = min(dp[i//3], dp[i-n]) + 1
            
    return dp[y] if dp[y] != float('inf') else -1