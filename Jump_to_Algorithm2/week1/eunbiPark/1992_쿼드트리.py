n = int(input())
board = [
    list(map(int, input()))
    for _ in range(n)
]

def dfs(x, y, n):
    if n == 1: # 최소 사각형
        ret.append(board[x][y])
        return

    stand = board[x][y] # 기준점
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != stand: # 기준과 다른 숫자 등장시
                n //= 2 # 분할정복
                ret.append('(')
                dfs(x, y, n) # 왼쪽 위
                dfs(x, y + n, n) # 오른쪽 위
                dfs(x + n, y, n) # 왼쪽 아래
                dfs(x + n, y + n, n) # 오른쪽 아래
                ret.append(')')
                return

    # 사각형이 한가지 숫자로만 이루어진 경우
    ret.append(stand)
    return

ret = []
dfs(0, 0, n)
print(*ret, sep = '')

'''
# sol_2
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input())))


def dfs(x, y, n):
    # 검사 범위 내 가장 첫번째 값을 기준점으로 잡기
    check = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != board[i][j]:
                check = -1
                break

    if check == -1:
        print('(', end='')
        n = n // 2
        dfs(x, y, n)
        dfs(x, y + n, n)
        dfs(x + n, y, n)
        dfs(x + n, y + n, n)
        print(')', end='')

    elif check == 1:
        print(1, end='')

    else:
        print(0, end='')

dfs(0, 0, n)
'''