import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
INF = int(1e9)
cost = {i: [] for i in range(1, N+1)}
min_cost = {i: INF for i in range(1, N+1)}

for _ in range(M):
    A, B, C = map(int, input().split())
    cost[A].append((B, C))
    cost[B].append((A, C))

min_cost[1] = 0
q = [(0, 1)]
heapq.heapify(q)

while q:
    c, l = heapq.heappop(q) # 현재까지 탐색한 길 중 최소비용이 드는 길에 대해 이어서 탐색
    if l == N: # 도착했다면 종료
        print(c)
        break
    for nl, nc in cost[l]: # l에서 갈 수 있는 선택지 중
        if min_cost[nl] > c + nc: # 지금까지 가본 1에서 nl까지 가는 방법 중 최소 비용이 드는 방법이라면
            min_cost[nl] = c + nc
            heapq.heappush(q, (c + nc, nl))
    
    
