# 미로탐색과 유사, 차이점: 벽을 부수는 횟수 -> 가중치
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
arr = [
    list(map(int, input()))
    for _ in range(n)
]

# 가중치
dist = [
    [-1] * m
    for _ in range(n)
]

q = deque()
q.append((0, 0))
dist[0][0] = 0
while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

print(dist[n-1][m-1])