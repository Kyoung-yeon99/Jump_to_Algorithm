import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

# 구간 출발점의 도시번호와 도착점의 도시번호
st, ed = map(int, input().split())

# 최단거리
dist = [INF] * (n + 1)


# 최단거리 구하기
def get_shortest(start):
    dist[start] = 0
    q = [(0, st)]

    while q:
        w, cur = heapq.heappop(q)
        if dist[cur] < w:  # 이미 계산되었다면
            continue
        for des, wei in graph[cur]:
            cost = dist[cur] + wei
            if dist[des] > cost:
                dist[des] = cost
                heapq.heappush(q, (cost, des))


get_shortest(st)
print(dist[ed])
