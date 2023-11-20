import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())

weight = [INF] * (V + 1)
heap = []
graph = [
    []
    for _ in range(V + 1)
]

def dijkstra(start):
    weight[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        wei, now = heapq.heappop(heap)

        if weight[now] < wei:
            continue

        for w, next_node in graph[now]:
            next_wei = w + wei

            if next_wei < weight[next_node]:
                weight[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dijkstra(K)
for i in range(1, V + 1):
    print('INF' if weight[i] == INF else weight[i])