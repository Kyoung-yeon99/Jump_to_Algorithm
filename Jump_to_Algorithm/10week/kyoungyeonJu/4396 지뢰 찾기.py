def bomb_cnt(a, b):
    cnt = 0
    for i in range(8):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < n and bomb[nx][ny] == '*':
            cnt += 1
    return cnt


n = int(input())
bomb = [list(input()) for _ in range(n)]  # 지뢰 위치
opens = [list(input()) for _ in range(n)]  # 열린 칸
result = [['.'] * n for _ in range(n)]
dx = [- 1, 0, 1, 1, 1, 0, - 1, - 1]
dy = [- 1, - 1, - 1, 0, 1, 1, 1, 0]
is_bomb = False

for i in range(n):
    for j in range(n):
        if opens[i][j] == 'x':
            if bomb[i][j] == '*':  # 지뢰를 열었으면
                is_bomb = True
                continue
            result[i][j] = bomb_cnt(i, j)

if is_bomb:
    for i in range(n):
        for j in range(n):
            if bomb[i][j] == '*':
                result[i][j] = '*'

for i in range(n):
    print(''.join(list(map(str, result[i]))))
