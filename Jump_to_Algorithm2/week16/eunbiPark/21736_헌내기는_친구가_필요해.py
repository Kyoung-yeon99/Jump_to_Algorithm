# O: 빈 공간, X: 벽, I: 도연, P: 사람
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

# 도연 위치 저장
for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            ix, iy = i, j

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

def bfs():
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] != 'X':
                if board[nx][ny] == 'P':
                    cnt += 1
                q.append((nx, ny))
                visited[nx][ny] = 1

    return cnt

# main
q = deque()
q.append((ix, iy))
visited[ix][iy] = 1
ans = bfs()
print(ans) if ans else print('TT')