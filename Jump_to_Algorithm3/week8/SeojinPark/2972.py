# 다익스트라
import heapq

INF = int(1e9)

n,m= map(int, input().split())
graph = [[] for i in range(n+1)]
cow=[INF]*(n+1)

for i in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))
    graph[y].append((x, z))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0, start))
    cow[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if cow[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost<cow[i[0]]:
                cow[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
print(cow[n])