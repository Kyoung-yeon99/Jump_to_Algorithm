n = int(input())
v = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs
visited = [0] * (n + 1)
cnt = 0

def dfs(start):
    global cnt
    # 방문처리
    visited[start] = 1
    # 인접 노드 방문, 재귀
    for node in graph[start]:
        if not visited[node]:
            cnt += 1
            dfs(node)

dfs(1)
print(cnt)