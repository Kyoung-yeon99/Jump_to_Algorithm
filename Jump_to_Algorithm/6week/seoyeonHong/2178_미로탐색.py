import sys
from collections import deque

n, m = map(int, input().split()) # 세로, 가로
a = []
for _ in range(n):
    a.append(list(sys.stdin.readline()))

visited = [[False for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
min_num = n * m

def bfs(): # 너비 우선 탐색 - 큐
    global min_num
    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    dp[0][0] = 1
    while q:
        pos = q.popleft()
        r, c = pos[0], pos[1]
        if r == n-1 and c == m-1:
            if min_num > dp[r][c]:
                min_num = dp[r][c]
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if a[nr][nc] == '1' and not visited[nr][nc]:
                    q.append([nr, nc])
                    visited[nr][nc] = True
                    dp[nr][nc] = dp[r][c] + 1

bfs()
print(min_num)