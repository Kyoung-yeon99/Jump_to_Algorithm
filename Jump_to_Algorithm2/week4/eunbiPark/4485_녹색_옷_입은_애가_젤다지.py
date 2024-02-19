# 도둑 루피를 획득하면 소지한 루피 감소
# 잃는 금액을 최소로 하여 동굴 건너까지 이동
# 링크가 잃을 수 밖에 없는 최소 금액

# => 도둑 루피를 최대한 만나지 않도록 이동, 이 때 만난 도둑 루피의 수

import heapq
import sys

input = sys.stdin.readline
inf = sys.maxsize

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def dijkstra(x, y):
    pq = []
    dist = [[inf] * n for _ in range(n)]

    heapq.heappush(pq, (graph[x][y], x, y))
    dist[x][y] = 0

    while pq:
        d, x, y = heapq.heappop(pq)

        if x == n -1 and y == n - 1: # 마지막 지점 도착
            return dist[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                nd = d + graph[nx][ny]

                if nd < dist[nx][ny]:
                    heapq.heappush(pq, (nd, nx, ny))
                    dist[nx][ny] = nd


test = 0
while 1:
    n = int (input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    test  += 1

    print(f"Problem {test}: {dijkstra(0, 0)}")
