from collections import deque

# 정점 개수, 간선개수, 탐색 시작할 정점 번호
n, m, v = map(int, input().split())
# 간선을 연결하는 두 정점 정보 저장
start_points = []
end_points = []

for _ in range(m):
    start_point, end_point = map(int, input().split())
    start_points.append(start_point)
    end_points.append(end_point)

# graph-> 0 based
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# 방문 처리
visited = [False for _ in range(n + 1)]


# dfs
def dfs(v):
    print(v, end=' ')  # 깊이 우선 탐색
    visited[v] = True  # 방문 처리

    # 현재 노드부터 n번 노드 까지 탐색
    for curr_v in range(1, n + 1):
        # 방문하지 않았고, 인접행렬의 값이 1이라면
        if not visited[curr_v] and graph[v][curr_v]:
            dfs(curr_v)


# bfs
def bfs(v):
    visited = [False for _ in range(n + 1)]  # bfs 방문체크용
    q = deque([v])  # deque 이용(양방향으로 삽입/삭제 가능: list보다 빠르다)
    visited[v] = True  # 방문 처리

    while q:
        curr_v = q.popleft()  # 큐에서 추출
        print(curr_v, end=' ')

        for nx in range(1, n + 1):
            # 방문하지 않았고, 인접행렬 값이 1이라면
            if not visited[nx] and graph[nx][curr_v]:
                q.append(nx)
                visited[nx] = True


# 양방향 그래프-> 인접행렬로 나타내기
for start, end in zip(start_points, end_points):
    graph[start][end] = 1
    graph[end][start] = 1

root_vertex = v
dfs(root_vertex)
print()
bfs(root_vertex)
