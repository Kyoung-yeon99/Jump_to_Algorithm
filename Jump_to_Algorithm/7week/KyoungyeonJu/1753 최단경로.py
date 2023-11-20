import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, v = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
dis = [INF] * (n+1)
for _ in range(v):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dis[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:  # 이미 최단거리가 계산된 노드라면
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if cost < dis[x[0]]:
                dis[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))


dijkstra(start)
for i in range(1, n+1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])
