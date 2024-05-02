# 1: 집 있음, 0: 집 없음
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

def bfs():
    cnt = 1 # 최단거리가 아니라 포함된 사람 수를 세야 함
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

# main
people = []
q = deque()
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j]:
            q.append((i, j))
            visited[i][j] = 1
            people.append(bfs())

people.sort()

print(len(people))
for p in people:
    print(p)