import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, m):
    q.append((0, 0))
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    total = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if cheese[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif cheese[nx][ny] == 1:
                    cheese[nx][ny] = 0
                    total += 1
                    visited[nx][ny] = 1
    return total


n, m = map(int, input().split())
cheese = [list(map(int, input().split)) for _ in range(n)]
c_list = []
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
while True:
    result = bfs(n, m)
    c_list.append(result)
    cnt += 1
    if sum(map(sum, cheese)) == 0:
        break

print(cnt)
print(c_list[-1])