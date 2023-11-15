import sys
sys.setrecursionlimit(100000)

n, m, k = map(int, input().split()) # 세로, 가로, 음식물 쓰레기 개수
foods = [[False for _ in range(m+1)] for _ in range(n+1)]
visited = [[False for _ in range(m+1)] for _ in range(n+1)]
max_size = 0
size = 0

for _ in range(k):
    r, c = map(int, input().split())
    foods[r][c] = True


def dfs(r, c): # 깊이 우선 탐색
    global size
    visited[r][c] = True
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 1 <= nr <= n and 1 <= nc <= m:
            if foods[nr][nc] and not visited[nr][nc]:
                dfs(nr, nc)
    size += 1

for r in range(1, n+1):
    for c in range(1, m+1):
        if foods[r][c] and not visited[r][c]:
            size = 0
            dfs(r, c)
            if size > max_size:
                max_size = size

print(max_size)