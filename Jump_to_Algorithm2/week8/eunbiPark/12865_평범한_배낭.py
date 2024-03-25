import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# dp[i][j] : i 번째 가방을 넣거나 뺐을 때 가능한 최대 무게
dp = [[0] * (k + 1) for _ in range(n + 1)]

things = [(0, 0)] # j == 0 은 비울 것임
for _ in range(n):
    things.append(tuple(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = things[i][0]
        v = things[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])

print(dp[n][k])
