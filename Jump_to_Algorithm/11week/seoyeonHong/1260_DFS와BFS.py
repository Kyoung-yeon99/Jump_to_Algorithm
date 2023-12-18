from collections import deque
import sys

input = sys.stdin.readline
n, m, v = map(int, input().split()) # 정점 개수, 간선 개수, 시작 정점
graph = dict({i: [] for i in range(1, n+1)})
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n+1): # 작은 번호의 정점부터 방문하기 위해 오름차순 정렬
    graph[i].sort()

visited = [False for _ in range(n+1)]

def dfs(cv): # 깊이 우선 탐색
    visited[cv] = True
    print(cv, end=' ')
    for nv in graph[cv]:
        if not visited[nv]:
            dfs(nv)

def bfs(): # 넓이 우선 탐색
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        cv = q.popleft()
        print(cv, end=' ')
        for nv in graph[cv]:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)

dfs(v)
visited = [False for _ in range(n+1)]
print()
bfs()
