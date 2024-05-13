from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    q.append((x, y))
    maps[x][y] = 1
    cnt = 1
    while q:
        xx, yy = q.popleft()
        for i in range(4):
            nx, ny = xx + dx[i], yy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if maps[nx][ny] == 0:
                    maps[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += 1
    return cnt


m, n, k = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
rects = []
for _ in range(k):
    c1, r1, c2, r2 = map(int, input().split())
    rects.append([m-r2, m-r1, c1, c2])

maps = [[0]*n for _ in range(m)]
for rect in rects:
    for r in range(rect[0], rect[1]):
        for c in range(rect[2], rect[3]):
            maps[r][c] = 1

answers = []
for i in range(m):
    for j in range(n):
        if maps[i][j] == 0:
            answers.append(bfs(i, j))

answers.sort()
print(len(answers))
print(' '.join(map(str, answers)))
