from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [[] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
qu = deque()
qu.append((0, 0))

for i in range(n):
    row = list(map(int, input().strip()))  # sys 활용할거면 strip() 필요!
    maze[i] = row

while True:
    x, y = qu.popleft()
    print("x=",x,"y=",y)
    if x == n-1 and y == m-1:
        print(maze[x][y])
        break
    for i in range(4):  # 상, 하, 좌, 우
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            qu.append((nx, ny))
            print("nx=",nx,"ny=",ny,"maze[nx][ny]=",maze[nx][ny], qu)

