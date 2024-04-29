import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(start)
visited = [0] * (n + 1)

def bfs():
    while q:
        curr = q.popleft()
        for c in graph[curr]:
            if not visited[c]:
                visited[c] = visited[curr] + 1
                q.append(c)

bfs()
print(-1) if not visited[end] else print(visited[end])