import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*6)


def dfs(n):
    visited[n] = True
    print(n, visited)

    for i in g[n]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

    return 1

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

visited = [False]*(n+1)
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
       c = dfs(i)
       cnt += c
       print(c, cnt)

print(cnt)
