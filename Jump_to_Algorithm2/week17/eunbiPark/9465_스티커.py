import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    board = [
        list(map(int, input().split()))
        for _ in range(2)
    ]

    # dp[i][j]: (i, j) 스티커를 떼었을 때 최대 점수
    dp = [[0 for _ in range(n)] for _ in range(2)]

    # 초기화
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]

    if n > 1:
        dp[0][1] = dp[1][0] + board[0][1]
        dp[1][1] = dp[0][0] + board[1][1]

    # 점화식
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + board[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + board[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))