import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)

def dfs(s):
    for child in graph[s]:
        if visited[child]==0:
            visited[child]=s
            # 자식 트리 재탐색
            dfs(child)

dfs(1)

for i in range(2,n+1):
    print(visited[i])