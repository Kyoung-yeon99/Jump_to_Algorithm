# 정점 개수 n
from collections import deque

n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]


def bfs(start):
    # 1. 큐
    q = deque()
    q.append(start)

    # 2. 큐에 빌때까지
    while q:
        # 큐에서 하나 빼기
        a = q.popleft()
        for i in range(n):
            if not visited[start][i] and adj[a][i]:  # 방문하지 않았고, 간선 존재한다면
                q.append(i)
                visited[start][i] = 1


visited = [[0] * n for _ in range(n)]

for i in range(n):
    bfs(i)

for i in visited:
    print(*i)
