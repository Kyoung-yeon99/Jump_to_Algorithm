import copy

m, n = map(int, input().split())
growth = [
    # 0, 1, 2 성장 개수
    list(map(int, input().split()))
    for _ in range(n)
]

board = [
    [1] * m
    for _ in range(m)
]

# 스스로 성장
def first_growth(growth_list):
    # 일자별 성장 배열 생성
    g_list = ([0] * growth_list[0]) + ([1] * growth_list[1]) +([2] * growth_list[2])

    row = g_list[:m-1]
    origin = g_list[m-1]
    col = g_list[m:]

    # 성장
    for i in range(m-1):
        # 열
        board[m-i-1][0] += row[i]
        # 행
        board[0][i + 1] += col[i]
    # 원점
    board[0][0] += origin

# 가장 큰 값 성장
def second_growth(temp_board):
    for i in range(1, m):
        for j in range(1, m):
            # 차이 계산 (l: 왼쪽, d: 왼쪽 위, u: 위쪽)
            l = board[i][j-1] - temp_board[i][j-1]
            d = board[i-1][j-1] - temp_board[i-1][j-1]
            u = board[i-1][j] - temp_board[i-1][j]
            # max 값 만큼 성장
            board[i][j] += max(l, d, u)
# main
for i in range(n):
    # 성장 차이 확인 위해 깊은 복사
    temp_board = copy.deepcopy(board)
    # 스스로 성장
    first_growth(growth[i])
    # 가장 큰 값 성장
    second_growth(temp_board)

for b in board:
    print(*b)