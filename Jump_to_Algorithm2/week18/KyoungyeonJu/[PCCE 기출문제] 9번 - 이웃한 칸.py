def solution(board, h, w):
    n, answer = len(board), 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]  # 오른쪽, 위, 아래, 왼쪽

    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                answer += 1

    return answer