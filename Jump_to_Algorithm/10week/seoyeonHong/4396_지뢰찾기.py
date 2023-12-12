n = int(input())
info = []
opened = []
board = [['.' for _ in range(n)] for _ in range(n)]
for _ in range(n):
    info.append(input())
for _ in range(n):
    opened.append(input())

def count_mine(row, column): # 주변의 지뢰 개수 반환
    count = 0
    for r in range(row-1, row+2):
        if r >= 0 and r < n:
            for c in range(column-1, column+2):
                if c >= 0 and c < n:
                    if info[r][c] == '*':
                        count += 1
    return str(count)

def reveal(): # 지뢰를 밟았을 경우 모든 지뢰 표시
    global board
    for r in range(n):
        for c in range(n):
            if info[r][c] == '*':
                board[r][c] = '*'

for r in range(n):
    for c in range(n):
        if opened[r][c] == 'x':
            if info[r][c] == '*':
                reveal()
            else:
                board[r][c] = count_mine(r, c)

for b in board:
    print(''.join(b))