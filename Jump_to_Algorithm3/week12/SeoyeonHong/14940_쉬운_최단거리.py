import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
l = []
found_destination = False
sr, sc = 0, 0
for r in range(n):
    row = list(map(int, input().split()))
    if not found_destination: # 목표지점 찾기
        for c in range(m):
            if row[c] == 2:
                sr, sc = r, c
                found_destination = True
                break
    l.append(row)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
visited = [[False for _ in range(m)] for _ in range(n)]
q = deque([[sr, sc, 0]])
l[sr][sc] = 0
visited[sr][sc] = True
while q: # bfs
    r, c, d = q.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and l[nr][nc] > 0:
            l[nr][nc] = d+1
            visited[nr][nc] = True
            q.append([nr, nc, d+1])

for r in range(n):
    for c in range(m):
        if l[r][c] == 1 and not visited[r][c]: # 갈 수 없는 땅인 경우
            l[r][c] = -1
        
for row in l:
    print(*row)
            
                

