from collections import deque


def dfs(graph, start, visited):
    visited[start] = True  # 방문 처리
    print(start, end=' ')
    for i in graph[start]:  # 인접노드 확인
        if not visited[i]:  # 방문하지 않았다면
            dfs(graph, i, visited_d)


def bfs(graph, start, visited):
    qu = deque([start])  # 큐 삽입
    print("첫번째줄 qu", qu)
    visited[start] = True  # 방문처리
    while qu:
        print("while 안 첫번째줄 qu", qu)
        n = qu.popleft()  # 큐 삭제
        print(n, end=' ')
        print("삭제 후 qu", qu)
        for i in graph[n]:  # 인접노드 확인
            if not visited[i]:  # 방문하지 않았다면
                qu.append(i)  # 큐 삽입
                visited[i] = True  # 방문처리


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_d = [False] * (N+1)
visited_b = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()  # 정점 번호가 작은 것부터 방문하기 위해 정렬
    graph[b].append(a)
    graph[b].sort()  # 정점 번호가 작은 것부터 방문하기 위해 정렬

print(graph)
dfs(graph, V, visited_d)
print()
bfs(graph, V, visited_b)



