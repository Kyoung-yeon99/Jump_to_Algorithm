import sys
import heapq

INF = 3000000
V, E = map(int, sys.stdin.readline().split()) # 정점의 개수, 간선의 개수
K = int(sys.stdin.readline()) # 시작 정점의 번호
graph = [[] for _ in range(V+1)] # 인접 노드 리스트
sp = [INF for _ in range(V+1)] # 최단 거리

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
print("graph ", graph)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    sp[start] = 0
    while q:
        dist, cur = heapq.heappop(q)
        print("pop: ", cur, dist)
        if sp[cur] < dist:
            continue
        for cv, cw in graph[cur]:
            cost = sp[cur] + cw
            if cost < sp[cv]:
                sp[cv] = cost
                heapq.heappush(q, (cost, cv))
                print("push: ", cv, cost)

dijkstra(K)

for i in range(1, V+1):
    if sp[i] == INF:
        print("INF")
    else:
        print(sp[i])