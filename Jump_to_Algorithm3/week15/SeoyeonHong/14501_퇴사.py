import sys

input = sys.stdin.readline
N = int(input())
counsel = []
dp = [0] * (N+1)

for _ in range(N):
    counsel.append(list(map(int, input().split())))

for d in range(N-1, -1, -1): # 뒤에서부터
    t, p = counsel[d][0], counsel[d][1]
    if d+t <= N: # 상담이 가능하다면
        dp[d] = max(dp[d+t:]) + p # 최대 금액 저장

print(max(dp))