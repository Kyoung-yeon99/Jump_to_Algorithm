from collections import deque
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

# 도치, 비버의 위치
for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            x, y = i, j
        elif board[i][j] == 'D':
            ex, ey = i, j

def in_range(x, y):
    if x < 0 or x >= r or y < 0 or y >= c:
        return False
    return True

def water():
    waters = [
        (i, j)
        for i in range(r)
        for j in range(c)
        if board[i][j] == '*'
    ]

    # 확산
    for x, y in waters:
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and board[nx][ny] == '.':
                board[nx][ny] = '*'

def bfs():
    step = 0
    while q:
        x, y = q.popleft()

        # 시간이 같다면 물이 퍼지지 않도록
        if step != visited[x][y]:
            step += 1
            # 물 확산 - 이동하기 전 처리
            water()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if (nx, ny) == (ex, ey):
                visited[nx][ny] = visited[x][y] + 1
                return #### break이면 안된다

            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == '.':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

q = deque()
q.append((x, y))
visited[x][y] = 0
water()
bfs()

print('KAKTUS') if not visited[ex][ey] else print(visited[ex][ey])

'''
5 5
.....
..XD.
..XXX
.....
S....

ans: 8
'''