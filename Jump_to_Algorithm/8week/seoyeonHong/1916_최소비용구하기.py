# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용
from collections import deque
import sys

n = int(sys.stdin.readline()) # 도시의 개수
m = int(sys.stdin.readline()) # 버스의 개수
INF = 100000000
graph = [[INF for _ in range(n+1)] for _ in range(n+1)] # 버스 정보(인접 행렬)

for _ in range(m):
    s, d, c = map(int, sys.stdin.readline().split()) # 출발 도시, 도착 도시, 비용
    if c < graph[s][d]: # A 에서 B로 가는 최소 비용만 저장
        graph[s][d] = c

start, dest = map(int, sys.stdin.readline().split()) # 구하고자 하는 구간 출발점, 도착점
total_cost = [INF for _ in range(n+1)]
min_cost = INF
q = deque()
q.append((start, 0))

while q:
    city, cost = q.popleft()
    if city == dest and cost < min_cost: # 도착점이고 총 비용이 지금까지 최소 비용일 경우 저장
        min_cost = cost
    for i in range(n+1):
        next_cost = graph[city][i]
        if next_cost != INF: # 현재 도시에서 갈 수 있는 도시일 경우
            new_cost = cost + next_cost
            if new_cost < min_cost and new_cost < total_cost[i]: # 현재까지 구한 최소비용 이하이고 next_city까지가는 최소 비용일 경우
                q.append((i, new_cost))
                total_cost[i] = new_cost

print(min_cost)

# 주의할 점 INF 값, 출발 지점과 도착 지점이 같은 버스가 여러개일 수 있음, 비용이 0일 수 있음

# 시간 초과 - 인접 행렬
# from collections import deque
# import sys

# n = int(sys.stdin.readline()) # 도시의 개수
# m = int(sys.stdin.readline()) # 버스의 개수
# graph = [[] for _ in range(n+1)] # 버스 정보(인접 노드 리스트)

# for _ in range(m):
#     s, d, c = map(int, sys.stdin.readline().split()) # 출발 도시, 도착 도시, 비용
#     graph[s].append((d, c))

# start, dest = map(int, sys.stdin.readline().split()) # 구하고자 하는 구간 출발점, 도착점
# total_cost = [100000 for _ in range(n+1)]
# min_cost = 100000
# q = deque()
# q.append((start, 0))

# while q:
#     city, cost = q.popleft()
#     if city == dest and cost < min_cost: # 도착점이고 총 비용이 지금까지 최소 비용일 경우 저장
#         min_cost = cost
#     for next_city, next_cost in graph[city]: # 현재 도시에서 갈 수 있는 곳 탐색
#         new_cost = cost + next_cost
#         if new_cost < min_cost and new_cost < total_cost[next_city]: # 현재까지 구한 최소비용 이하이고 next_city까지가는 최소 비용일 경우
#             q.append((next_city, new_cost))
#             total_cost[next_city] = new_cost

# print(min_cost)

