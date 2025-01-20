# N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간
import sys
import heapq

input = sys.stdin.readline
N, M, X = map(int, input().split())
INF = int(1e9)
load = [[] for _ in range(N+1)]
load_reversed = [[] for _ in range(N+1)]
max_time = 0

def dijkstra(l, X): # X에서 각 정점까지 가는데 걸리는 최소시간
    min_time = [INF for _ in range(N+1)] # min_time[i]: i번째 정점까지 가는데 걸리는 최소시간
    min_time[X] = 0
    q = [(0, X)]
    heapq.heapify(q)
    while q:
        total_time, A = heapq.heappop(q)
        for B, time in l[A]:
            if min_time[B] > total_time + time:
                min_time[B] = total_time + time
                heapq.heappush(q, (min_time[B], B))
    return min_time
                

for _ in range(M):
    s, e, t = map(int, input().split())
    load[s].append((e, t))
    load_reversed[e].append((s, t))

from_X = dijkstra(load, X) # X에서 모든 정점까지의 최단 시간, 정방향 그래프 + 다익스트라
to_X = dijkstra(load_reversed, X) # 모든 정점에서 X까지의 최단 시간, 역방향 그래프 + 다익스트라
max_time = max(to_X[i] + from_X[i] for i in range(1, N+1))
    
print(max_time)

