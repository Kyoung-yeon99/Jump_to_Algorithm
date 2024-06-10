# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    n = len(board)
    count = 0 # 이웃한 칸들 중 같은 색으로 색칠되어 있는 칸의 수
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count