# import heapq
# import sys
#
#
# def dijkstra(graph, start):
#     distances = [float('inf')] * len(graph)
#     distances[start] = 0
#     queue = [(0, start)]
#
#     print(f"\n노드 {start}에서 다익스트라 알고리즘 시작")
#
#     while queue:
#         current_distance, current_node = heapq.heappop(queue)
#         print(f"노드 {current_node} 처리 중, 현재 거리: {current_distance}")
#
#         if distances[current_node] < current_distance:
#             continue
#
#         for neighbor, weight in graph[current_node]:
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(queue, (distance, neighbor))
#                 print(f"  노드 {neighbor}까지의 거리 업데이트: {distance}")
#
#     return distances
#
#
# # 입력 처리
# n, m, x = 4, 8, 2
# roads = [
#     (1, 2, 4),
#     (1, 3, 2),
#     (1, 4, 7),
#     (2, 1, 1),
#     (2, 3, 5),
#     (3, 1, 2),
#     (3, 4, 4),
#     (4, 2, 3)
# ]
#
# print("입력 데이터:")
# print(f"마을 수: {n}")
# print(f"도로 수: {m}")
# print(f"파티 위치: {x}")
# print("도로 정보:", roads)
#
# # 그래프 생성
# graph = [[] for _ in range(n + 1)]
# reverse_graph = [[] for _ in range(n + 1)]
#
# for start, end, time in roads:
#     graph[start].append((end, time))
#     reverse_graph[end].append((start, time))
#
# print("\n그래프:", graph)
# print("역방향 그래프:", reverse_graph)
#
# # X에서 각 마을로 가는 최단 시간 계산
# print("\nX에서 각 마을로 가는 최단 거리 계산:")
# from_x = dijkstra(graph, x)
# print("X에서의 최단 거리:", from_x)
#
# # 각 마을에서 X로 가는 최단 시간 계산
# print("\n각 마을에서 X로 가는 최단 거리 계산:")
# to_x = dijkstra(reverse_graph, x)
# print("X로의 최단 거리:", to_x)
#
# # 왕복 시간 계산 및 최대값 찾기
# print("\n왕복 시간 계산:")
# max_time = 0
# round_trip_times = []
# for i in range(1, n + 1):
#     round_trip = from_x[i] + to_x[i]
#     round_trip_times.append(round_trip)
#     print(f"학생 {i}의 왕복 시간: {round_trip}")
#     max_time = max(max_time, round_trip)
#
# print("\n모든 학생의 왕복 시간:", round_trip_times)
# print("최대 왕복 시간:", max_time)

import heapq
import sys

def dijkstra(g, start):
    time= [float('inf')] * len(g)
    time[start] = 0 #시작 마을 소요시간은 0
    q = [(0, start)] # (시간, 방문노드)

    while q:
        #현재 소요시간, 마을 하나 꺼내기 - heapq 사용으로 가장 가까운 곳부터 반환
        cur_t, cur_node = heapq.heappop(q)
        #더 짧은 시간이 걸린다면 continue
        if time[cur_node] < cur_t:
            continue

        #연결된 마을 탐색
        for n, t in g[cur_node]:
            n_t = cur_t + t #현재 마을 까지 시간 + 연결된 마을 시간 계산
            if n_t < time[n]: #기존 거리보다 짧으면
                time[n] = n_t #업데이트
                heapq.heappush(q, (n_t, n)) #heapq에 추가하기

    return time #각 마을까지 최단 시간 담은 리스트 반환


N, M, X = map(int, sys.stdin.readline().split())
g = [[] for _ in range(N+1)] #인접 리스트 : 집 -> X
back_g = [[] for _ in range(N+1)] #인접 리스트 : X - > 집

for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    g[start].append((end, time))
    back_g[end].append((start, time))

# X에서 각 마을로 가는 최단 시간 계산
go = dijkstra(g, X)

# 각 마을에서 X로 가는 최단 시간 계산
back = dijkstra(back_g, X)

# 왕복 시간 계산 및 최대값 찾기
max_time = 0
for i in range(1, N+1):
    total = go[i] + back[i]
    max_time = max(max_time, total)

# 결과 출력
print(max_time)
