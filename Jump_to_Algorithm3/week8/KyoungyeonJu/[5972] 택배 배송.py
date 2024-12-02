# n개의 헛간(노드), m개의 소들의 양방향 길(간선), 각각의 길에 c마리의 소
# 두 개의 헛간은 하나 이상의 길로 연결되어 있을 수 있다
# 최소 간선 비용
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dis = [INF]*(n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])  # a번 노드에서 b번 노드로 가는 비용 c
    graph[b].append([a, c])  # b번 노드에서 a번 노드로 가는 비용 c


q = []
heapq.heappush(q, (0, 1))  # 거리, 노드
dis[1] = 0
while q:
    dist, now = heapq.heappop(q)
    if dis[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < dis[i[0]]:
            dis[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))  # 거리, 노드

print(dis[n])
