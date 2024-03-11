import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[] for _ in range(n + 1)]
ret = []

for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)


def bfs(v):
    while q:
        c = q.popleft()
        for j in board[c]:
            if not visited[j]:
                visited[j] = visited[c] + 1
                q.append(j)

for i in range(1, n + 1):
    q = deque()
    q.append(i)

    visited = [0] * (n + 1)
    visited[i] = 1

    bfs(i)
    ret.append(sum(visited))

print(ret.index(min(ret)) + 1)