from sys import stdin
import heapq

N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

meal = [float('inf')] * (N + 1)
previous = [0] * (N + 1)  # 각 노드의 이전 노드를 저장하는 배열
queue = []
heapq.heappush(queue, (0, 1))
meal[1] = 0

while queue:
    current_meal, current_position = heapq.heappop(queue)
    if current_position == N:
        break
    if current_meal > meal[current_position]:
        continue
    for next_position, cost in graph[current_position]:
        next_meal = current_meal + cost
        if next_meal < meal[next_position]:
            meal[next_position] = next_meal
            previous[next_position] = current_position  # 이전 노드 기록
            heapq.heappush(queue, (next_meal, next_position))

# 최적 경로 역추적
print(previous)
path = []
current = N
while current != 0:
    path.append(current)
    current = previous[current]
path.reverse()

print(f"최소 여물: {meal[N]}")
print(f"최적 경로: {' -> '.join(map(str, path))}")