from collections import deque
n, m, k = map(int, input().split())
board = [[0 for _ in range(m)]for _ in range(n)]
visited = [[0 for _ in range(m)]for _ in range(n)]
ans = []

for _ in range(k):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

def bfs():
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and not board[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if not visited[i][j] and not board[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = 1
            ans.append(bfs())

ans.sort()
print(len(ans))
print(*ans)