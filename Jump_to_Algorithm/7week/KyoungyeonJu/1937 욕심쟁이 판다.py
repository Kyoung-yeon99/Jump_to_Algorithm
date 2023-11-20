def sum(x, y):
    print("x=",x,"y=",y)
    if visited[x][y]:  # 이미 계산한 경로여서 0이 아니면 return
        return visited[x][y]
    visited[x][y] = 1  # 처음 들어오면 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and bb[nx][ny] > bb[x][y]:  # 범위 확인, 대나무 비교
            #print(visited[x][y])
            visited[x][y] = max(visited[x][y], sum(nx, ny)+1)
            #print("x=", x, "y=", y, "nx=", nx, "ny=", ny,"visited[x][y]=", visited[x][y], "sum(nx,ny)=", visited[nx][ny])
    return visited[x][y]


n = int(input())
bb = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*n for _ in range(n)]  # 해당 위치에서 시작해서 갈 수 있는 최대 이동 수
max_b = 0
for i in range(n):
    for j in range(n):
        max_b = max(max_b, sum(i, j))
print(max_b)

for i in range(n):
    print(visited[i])


""" 시간 초과
from collections import deque
def bfs(x, y):
    qu = deque()
    qu.append((x, y))
    visited[x][y] = 1

    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and bb[nx][ny] > bb[x][y]:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                else:
                    visited[nx][ny] = max(visited[nx][ny], visited[x][y] + 1)
                qu.append((nx, ny))
                #print("x=", x, "y=", y, "nx=", nx, "ny=", ny,"visited[x][y]=", visited[x][y], "visited[nx][ny]=", visited[nx][ny])


n = int(input())
bb = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)

for i in range(n):
    print(visited[i])

max_b = 0
for row in visited:
    if max_b < max(row):
        max_b = max(row)
print(max_b)
"""