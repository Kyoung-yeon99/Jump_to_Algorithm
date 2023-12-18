from collections import deque
n = int(input())
board = [[0]*n for _ in range(n)]
a_num = int(input())
for _ in range(a_num):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2

d_num = int(input())
direction = dict()
for _ in range(d_num):
    s, d = input().split()
    direction[int(s)] = d

dx = [0, 1, 0, -1]  # 오른쪽, 아래쪽, 왼쪽, 위쪽
dy = [1, 0, -1, 0]
qu = deque()
qu.append((0, 0))
x, y = 0, 0
board[x][y] = 1
sec = 0  # 초 세기
direct = 0

while True:
    sec += 1
    x += dx[direct]
    y += dy[direct]
    if x < 0 or x >= n or y < 0 or y >= n:  # 벽 부딪히면
        break
    if board[x][y] == 2:  # 사과가 있다면
        board[x][y] = 1
        qu.append((x, y))
        if sec in direction:
            if direction[sec] == 'L':  # 왼쪽으로 90도 회전
                direct = (direct - 1) % 4
            else:  # 오른쪽으로 90도 회전
                direct = (direct + 1) % 4

    elif board[x][y] == 0:  # 아무것도 없다면
        board[x][y] = 1
        qu.append((x, y))
        tx, ty = qu.popleft()
        board[tx][ty] = 0  # 꼬리 위치한 칸 비우기
        if sec in direction:
            if direction[sec] == 'L':
                direct = (direct - 1) % 4
            else:
                direct = (direct + 1) % 4
    else:
        break

print(sec)
