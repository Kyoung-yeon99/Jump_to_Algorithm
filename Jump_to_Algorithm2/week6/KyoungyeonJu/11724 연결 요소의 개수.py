import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 안하면 런타임에러 RecursionError


def dfs(n):
    visited[n] = True  # 방문처리
    # print(n, visited)

    for i in g[n]:  # 정점 n에 연결된 정점들 확인
        if not visited[i]:  # 방문하지 않은 곳 찾아서 방문
            dfs(i)

    return True


n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

visited = [False]*(n+1)
cnt = 0
for i in range(1, n+1):
    if not visited[i]:  # 방문하지 않은 곳만
        if dfs(i):
            cnt += 1
            # print(cnt)

print(cnt)
