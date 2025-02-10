import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
visited = [[False for _ in range(m)] for _ in range(n)]
count = 0
max_area = 0
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]

def calculate_area(r, c): # 그림의 면적 계산, 너비 우선 탐색
    q = deque([(r, c)])
    visited[r][c] = True
    area = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if paper[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    area += 1
    return area

for r in range(n):
    for c in range(m):
        if paper[r][c] == 1 and not visited[r][c]:
            max_area = max(max_area, calculate_area(r, c))
            count += 1

print(count)
print(max_area)