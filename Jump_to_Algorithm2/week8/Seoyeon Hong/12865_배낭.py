# 배낭에 넣을 수 있는 물건들의 가치의 최댓값
import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 물품의 수, 최대 무게
thing = [[0, 0]]
for _ in range(N):
    thing.append(list(map(int, input().split())))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# knapsack 알고리즘
for r in range(1, N+1):
    w = thing[r][0]
    v = thing[r][1]
    for c in range(1, K+1):
        if w <= c:
            dp[r][c] = max(dp[r-1][c], dp[r-1][c-w]+v)
        else:
            dp[r][c] = dp[r-1][c]

print(dp[-1][-1])


# 오답
# import sys

# input = sys.stdin.readline

# N, K = map(int, input().split()) # 물품의 수, 최대 무게
# weight, value = [], [] # 물품의 무게, 가치

# max_value = 0
# for i in range(N):
#     W, V = map(int, input().split())
#     if W <= K: # 최대 무게보다 작을 경우만 배낭에 넣을 수 있음
#         weight.append(W)
#         value.append(V)

# N = len(weight)

# if N == 0:
#     print(0)
# else:
#     dp = [0 for _ in range(N)] # i를 포함하면서 만들 수 있는 가치의 최댓값

#     def pick(w, v, bag):
#         print(bag, dp)
#         global max_value
#         for i in range(N):
#             if i not in bag:
#                 nw = w + weight[i]
#                 if nw <= K:
#                     nv = v + value[i]
#                     if nv > dp[i]:
#                         nb = bag.copy()
#                         nb.append(i)
#                         dp[i] = nv
#                         pick(nw, nv, nb)

#     for p in range(N):
#         dp[p] = value[p]
#         pick(weight[p], value[p], [p])

#     print(max(dp))