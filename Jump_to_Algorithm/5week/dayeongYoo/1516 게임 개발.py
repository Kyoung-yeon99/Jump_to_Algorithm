import sys
from collections import deque

q = deque()
n = int(input())
indegree = [0] * (n + 1)
times = [0] * (n + 1)
dp = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    tower = list(map(int, input().split()))
    times[i] = tower[0]
    if len(tower) > 2:
        for j in tower[1:-1]:
            graph[j].append(i)
            indegree[i] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = times[i]

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[i], dp[now] + times[i])
        if indegree[i] == 0:
            q.append(i)

for i in dp:
    if i != 0:
        print(i)
