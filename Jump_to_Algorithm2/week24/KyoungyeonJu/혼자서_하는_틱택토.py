def solution(board):
    tboard = list(map(list, zip(*board)))  # 전치
    WIN_O, WIN_X = False, False

    # 가로, 세로 확인
    for i in range(3):
        if board[i] == "OOO" or ''.join(tboard[i]) == "OOO":
            WIN_O = True
        elif board[i] == "XXX" or ''.join(tboard[i]) == "XXX":
            WIN_X = True

    # 대각선 확인
    if [board[0][0], board[1][1], board[2][2]] == ["O"] * 3 or [board[0][2], board[1][1], board[2][0]] == ["O"] * 3:
        WIN_O = True
    if [board[0][0], board[1][1], board[2][2]] == ["X"] * 3 or [board[0][2], board[1][1], board[2][0]] == ["X"] * 3:
        WIN_X = True

    # 개수 구하기
    cnt_o, cnt_x = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                cnt_o += 1
            if board[i][j] == "X":
                cnt_x += 1

    if cnt_o < cnt_x or cnt_o != cnt_x + 1:  # x개수는 o개수보다 많을 수 없다. o개수는 x개수보다 1개 초과 많을 수 없다
        return 0
    elif WIN_O and WIN_X:  # 동시 우승 불가능
        return 0
    elif WIN_O and cnt_o != (cnt_x + 1):  # o가 이기면 o개수는 x개수보다 하나 많다
        return 0
    elif WIN_X and cnt_o != cnt_x:  # x가 이기면, x개수와 o개수는 같다
        return 0

    return 1


"""
    # 함수 활용 코드  
    # 승리 조건 확인 함수
    def check_win(player):
        tboard = list(map(list, zip(*board)))
        # 가로, 세로
        for i in range(3):
            if board[i] == player*3 or ''.join(tboard[i]) == player*3:
                return True

        # 대각선
        if [board[0][0], board[1][1], board[2][2]] == [player] * 3 or [board[0][2], board[1][1], board[2][0]] == [player] * 3:
            return True

        return False


    # O와 X의 개수 세기
    cnt_o = sum(row.count('O') for row in board)
    cnt_x = sum(row.count('X') for row in board)

    # x개수는 o개수보다 많을 수 없다. o개수는 x개수보다 1 초과 많을 수 없다
    if cnt_o < cnt_x or cnt_o > cnt_x + 1:
        return 0

    # 승패 확인
    WIN_O = check_win('O')
    WIN_X = check_win('X')

    if WIN_O and WIN_X:  # 동시 우승 불가능
        return 0
    elif WIN_O and cnt_o != (cnt_x + 1):  # o가 이기면, o개수는 x개수보다 하나 많다
        return 0
    elif WIN_X and cnt_o != cnt_x:  # x가 이기면, x개수와 o개수는 같다
        return 0

    return 1
"""
