import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = list(map(lambda x: int(x) - 1, input().split()))

# 우, 좌, 상, 하
dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

dice = [0] * 7 # (idx: 주사위 위치, 값: 적힌 값)

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True

def move_dice(up, front, right, d):
    if d == 0: # 동
        temp_up = 7 - right
        temp_front = front
        temp_right = up
    elif d == 1: # 서
        temp_up = right
        temp_front = front
        temp_right = 7 - up
    elif d == 2: # 북
        temp_up = front
        temp_front = 7 - up
        temp_right = right
    elif d == 3: # 남
        temp_up = 7 - front
        temp_front = up
        temp_right = right

    return temp_up, temp_front, temp_right

# 인덱스 담기
up, front, right = 1, 5, 3

# main
for d in move:
    # 좌표 이동
    nx, ny = x + dxs[d], y + dys[d]
    if not in_range(nx, ny):
        continue

    # 주사위 이동
    up, front, right = move_dice(up, front, right, d)

    temp_dice = [0] * 7

    x, y = nx, ny
    if board[x][y] == 0:
        # 주사위 -> 바닥
        board[x][y] = dice[7-up]

    else:
        # 바닥 -> 주사위
        dice[7-up] = board[x][y]
        board[x][y] = 0

    print(dice[up])

