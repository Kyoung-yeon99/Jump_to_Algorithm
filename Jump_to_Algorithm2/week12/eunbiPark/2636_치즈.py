# 0: 공기, 1: 치즈
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cheese = [] # 남은 치즈 조각의 개수

# 공기면 탐색, 치즈면 공기로 바꾸고 방문처리
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    cnt = 0

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                if board[nx][ny] == 0: # 공기면
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif board[nx][ny] == 1: # 치즈면
                    board[nx][ny] = 0
                    cnt += 1 # 치즈 개수 세기
                    visited[nx][ny] = 1
                    # 큐에 추가 안해서 치즈 안으로 들어갈 수 없음

    cheese.append(cnt)
    return cnt

# main
time = 0
while 1:
    time += 1
    cnt = bfs()
    if cnt == 0:
        break

print(time - 1)
print(cheese[-2])