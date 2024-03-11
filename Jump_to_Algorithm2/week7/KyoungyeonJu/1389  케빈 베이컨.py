import heapq
import sys
input = sys.stdin.readline


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 거리, 노드
    dis[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in graph[now]:  # i[0] 도착노드 i[1] 거리비용
            cost = dist + i[1]
            if cost < dis[i[0]]:  # 더 짧은 거리라면 갱신
                dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n, m = map(int, input().split())
INF = int(1e9)
mini, mini_n = INF, 0
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))  # 모든 거리 비용은 1
    graph[b].append((a, 1))

for i in range(1, n+1):
    dis = [INF] * (n + 1)
    dijkstra(i)
    if mini > sum(dis[1:]):
        mini = sum(dis[1:])
        mini_n = i
    print(dis, sum(dis[1:]), mini, mini_n)

print(mini_n)
