import sys
from collections import deque
input = sys.stdin.readline


def bfs(bridge):
    q = deque()

    for i in range(n):
        for j in range(n):
            if maps[i][j] == bridge:
                q.append([i, j])
                dis[i][j] = 0 
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] != bridge and maps[nx][ny] != 0:
                    return dis[x][y]
                if maps[nx][ny] == 0 and dis[nx][ny] == -1:  # 물이고 건넌적 없는 곳
                    dis[nx][ny] = dis[x][y]+1
                    q.append([nx, ny])
    return 10**4


def island(x, y, num):
    q = deque()
    q.append([x, y])
    while q:
        xx, yy = q.popleft()
        maps[xx][yy] = num
        for i in range(4):
            nx, ny = xx+dx[i], yy+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = num
                    q.append([nx, ny])


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
min_num = 10**4
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

num = 2
for i in range(n):  # 섬마다 번호 다르게 지정
    for j in range(n):
        if maps[i][j] == 1:
            island(i, j, num)
            num += 1

for bridge in range(2, num):
    dis = [[-1] * n for _ in range(n)]
    result = bfs(bridge)
    min_num = min(min_num, result)

print(min_num)

