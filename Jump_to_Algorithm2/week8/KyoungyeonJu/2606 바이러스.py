from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
cnt = 0
q = deque([1])
while q:
    now = q.popleft()
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            q.append(next)

print(visited.count(True)-1)

