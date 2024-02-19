# D까지의 거리를 하나의 노드로 보기
# 각 노드 까지 거리를 1로 초기화
# 지름길 정보가 들어오면 graph에 정보 추가 (D 보다 크면 추가하지 않음)

#############풀이 1#############
# 다익스트라

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 위치 인덱스, 현재 위치

        #지금 힙큐에서 뺀게 now까지 가는데 최소비용이 아닐수도 있으니 체크
        if dist > distance[now]: # dist가 지금 힙 큐 에서 뺀 것 보다 크다: 지름길을 통해 가는 것 보다 그냥 가는 게 빠르다
            continue

        # 지름길이라면
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


n , d = map(int,input().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

# 거리 초기화
for i in range(d):
    graph[i].append((i+1, 1))

# 지름길 기록
for _ in range(n):
    s, e, l = map(int,input().split())
    if e > d: # 가야할 길을 넘어서기에 pass
        continue
    graph[s].append((e,l)) # graph에 지름길 추가

dijkstra(0)
print(distance[d])

#############풀이 2#############
# 유사 dfs

N, D = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)] # 지름길 정보
dis = [i for i in range(D+1)] # 최단 테이블 생성 [1, 2, 3, ..., D]
for i in range(D+1):
    if i > 0:
        dis[i] = min(dis[i], dis[i-1]+1) # 현재 테이블 vs 한 칸 전 테이블 값 + 1 -> 최솟값 판단

    # 지름길 판단
    for s, e, d in li:
        # i == s : 지름길 도착
        # e <= D : 지름길의 끝이 도착 목표 안에 존재
        # dis[i] + d : 현재 위치에서 지름길로 빠진 크기
        # dis[e] : 지름길의 끝 까지 그냥 가본 크기
        #  dis[i]+d < dis[e]: 지름길의 끝까지 가는 것 보다 현재 위치에서 지름길 크기를 더한 게 작다면
        if i == s and e <= D and dis[i]+d < dis[e]:
            dis[e] = dis[i]+d # 최솟값 갱신

print(dis[D])