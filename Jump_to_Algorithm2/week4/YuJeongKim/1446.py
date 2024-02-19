# 최단거리 -> 다익스트라
# 모든 노드 가중치 INF 설정, 가중치보다 작으면 경로 갱신
import heapq

n,d=map(int,input().split())

# i에서 갈 수 있는 노드
graph = [ [] for _ in range(d+1)]

for i in range(d):
    graph[i].append((i+1,1))

for _ in range(n):
    s,e,l=map(int,input().split())

    if e>d:
        continue

    graph[s].append((e,l))


INF = 987654321
# i까지 최소 비용
distance = [INF]*(d+1)

q=[]
heapq.heappush(q, (0,0))

while q:
    c, start = heapq.heappop(q)

    if distance[start] < c: continue

    # start에서 갈 수 있는 노드
    for node in graph[start]:
        cost = c + node[1]

        if distance[node[0]] > cost :
            distance[node[0]]=cost

            heapq.heappush(q, (cost, node[0]))

print(distance[d])