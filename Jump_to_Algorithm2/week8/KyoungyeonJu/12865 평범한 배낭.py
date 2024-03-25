import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)  # 용량이 i일 때, 담을 수 있는 최대 가치
weights, value = [], []

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    value.append(v)

for i in range(n):
    for j in range(k, weights[i]-1, -1):  # 용량 k에서 각 물건의 무게까지
       dp[j] = max(dp[j], dp[j-weights[i]]+value[i])

print(dp[-1])
