from collections import deque
def dfs(x):  # 넓이 우선 탐색
    visited_d[x] = True
    print(x, end=" ")
    for i in graph[x]:
        if not visited_d[i]:
            dfs(i)


def bfs(w):
    qu = deque([w])
    visited_b[w] = True
    while qu:
        y = qu.popleft()
        print(y, end=" ")
        for i in graph[y]:
            if not visited_b[i]:
                qu.append(i)
                visited_b[i] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_d = [False]*(n+1)
visited_b = [False]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)  # 양방향 간선
    graph[b].sort()

dfs(v)
print()
bfs(v)




