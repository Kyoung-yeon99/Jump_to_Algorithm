# 정점 개수, 간선개수, 탐색 시작할 정점 번호
from collections import deque

n, m, v = map(int, input().split())

# 간선을 연결하는 두 정점 정보 저장
start_points = []
end_points = []
for _ in range(m):
    start_point, end_point = map(int, input().split())
    start_points.append(start_point)
    end_points.append(end_point)

# graph
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# 방문 처리
visited = [False for _ in range(n + 1)]


# dfs
def dfs(v):
    print(v, end=' ')
    visited[v] = True

    for curr_v in range(1, n + 1):
        if not visited[curr_v] and graph[v][curr_v]:
            dfs(curr_v)


# bfs
def bfs(v):
    q = deque([v])
    visited[v] = False

    while q:
        curr_v = q.popleft()
        print(curr_v, end=' ')

        for i in range(1, n + 1):
            if visited[i] and graph[curr_v][i]:
                q.append(i)
                visited[i] = False


# 양방향 그래프
for start, end in zip(start_points, end_points):
    graph[start][end] = 1
    graph[end][start] = 1

root_vertex = v
dfs(root_vertex)
print()
bfs(root_vertex)