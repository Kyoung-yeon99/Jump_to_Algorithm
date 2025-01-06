# 위치를 옮기는 아이들의 수를 최소로 하기
# LIS

N = int(input())
kids = [int(input()) for _ in range(N)]
dp = [0]*N
dp[0] = 1
max_num = 0

for i in range(1, N):
    for j in range(i):
        if kids[i] > kids[j]:
            max_num = max(max_num, dp[j])
    dp[i] = max_num+1
    max_num = 0

print(N-max(dp))