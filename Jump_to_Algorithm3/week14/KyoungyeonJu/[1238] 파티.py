import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, v, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(v):
    a, b, c = map(int, input().split())  # 시작점, 끝점, 소요시간
    graph[a].append((b, c))
t = [0] * (n+1)

def dijkstra(s):
    global dis
    q = []
    heapq.heappush(q, (0, s))
    dis[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if cost < dis[x[0]]:
                dis[x[0]] = cost
                heapq.heappush(q, (cost, x[0]))


for i in range(1, n+1):
    dis = [INF] * (n + 1)
    dijkstra(i)
    if i == x:
        t = [x+y for x, y in zip(dis, t)]
    else:
        t[i] += dis[x]

print(max(t[1:]))




