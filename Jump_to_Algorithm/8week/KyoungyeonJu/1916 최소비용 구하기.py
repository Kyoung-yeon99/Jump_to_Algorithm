import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dis = [INF]*(n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())
q = []
heapq.heappush(q, (0, s))
dis[s] = 0
while q:
    dist, now = heapq.heappop(q)
    if dis[now] < dist: continue
    for x in graph[now]:
        cost = dist + x[1]
        if cost < dis[x[0]]:
            dis[x[0]] = cost
            heapq.heappush(q, (cost, x[0]))

print(dis[e])