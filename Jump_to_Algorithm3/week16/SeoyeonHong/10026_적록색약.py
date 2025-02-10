import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
painting = []

for _ in range(N):
    painting.append(list(input().rstrip()))

section = [0, 0]
visited = [[False for _ in range(N)] for _ in range(N)]
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(sr, sc, color): # 너비 우선 탐색
    global visited
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and painting[nr][nc] == color:
                q.append((nr, nc))
                visited[nr][nc] = True

for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            bfs(r, c, painting[r][c])
            section[0] += 1

for r in range(N):
    for c in range(N):
        if painting[r][c] == 'G': # 'G'를 'R'로 바꾸기
            painting[r][c] = 'R'

visited = [[False for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            bfs(r, c, painting[r][c])
            section[1] += 1

print(*section)

        



