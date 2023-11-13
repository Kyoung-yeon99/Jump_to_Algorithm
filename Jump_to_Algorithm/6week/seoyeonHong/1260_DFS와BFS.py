from collections import deque
vertexes, edges, root = map(int, input().split()) # 정점의 개수, 간선의 개수, 시작 정점
graph = [[] for _ in range(vertexes+1)]

for _ in range(edges):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for g in graph: # 오름차순 -> 정점 번호가 작은 것부터 방문
    g.sort()

visited = [False] * (vertexes + 1)

def dfs(v): # 깊이 우선 탐색 - 재귀함수
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v): # 너비 우선 탐색 - 큐
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        next = q.popleft()
        print(next, end=' ')
        for i in graph[next]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(root)
visited = [False] * (vertexes + 1)
print('')
bfs(root)