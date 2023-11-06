# 위상 정렬 + dp
# 건물 건설시 요구하는 건물들이 모두 완공
# 마지막 건설 건물 시간 + 어떤 건물의 건설 시간

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [
    []
    for _ in range(n + 1)
]
indegree = [0] * (n + 1)
cost = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))[:-1]
    cost[i] = tmp[0]
    for j in tmp[1:]:
        graph[j].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)
        dp[i] = cost[i]

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[now] + cost[i])

        if indegree[i] == 0:
            q.append(i)

for i in dp:
    if i != 0:
        print(i)