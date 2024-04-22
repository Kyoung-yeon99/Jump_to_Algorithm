n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] : (i, j) 에서의 합의 최댓값
dp = [[0 for _ in range(n)] for _ in range(n)]

# 초기화
dp[0][0] = board[0][0]
# 마스킹
for i in range(n):
    board[i].insert(0, -1)
    board[i].append(-1)

# 점화식 - dp[i][j] = max(dp[i-1][j], dp[i-1][j-1) + board[i][j]
for i in range(1, n):
    for j in range(1, i + 2):
        dp[i][j-1] = max(dp[i-1][j-1], dp[i-1][j-2]) + board[i][j]

print(max(dp[n-1]))