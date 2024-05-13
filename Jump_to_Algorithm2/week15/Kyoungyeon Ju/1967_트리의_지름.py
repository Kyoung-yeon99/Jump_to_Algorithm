import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(s, dis):
    for n, n_dis in graph[s]:
        if visited[n] == -1:
            visited[n] = dis + n_dis
            dfs(n, dis+n_dis)


n = int(input())
visited = [-1]*(n+1)
visited[1] = 0
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    graph[p].append([c, w])
    graph[c].append([p, w])

dfs(1, 0)  # 루트 노드에서 가장 먼 노드 구하기
far_node = visited.index(max(visited))
visited = [-1]*(n+1)
visited[far_node] = 0
dfs(far_node, 0)  # 루트 노드에서 가장 먼 노드에서 가장 먼 노드 구하기

print(max(visited))