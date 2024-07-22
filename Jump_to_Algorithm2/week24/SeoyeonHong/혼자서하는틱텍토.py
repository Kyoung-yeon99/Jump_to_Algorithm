# https://school.programmers.co.kr/learn/courses/30/lessons/160585

# 게임판이 규칙을 지켜서 진행한 틱택토에서 나올 수 있는 상황인지 판단
def solution(board):
    winner = []
    for r in range(3): # 행 확인
        if board[r] == 'OOO':
            winner.append('O')
        elif board[r] == 'XXX':
            winner.append('X')
    for c in range(3): # 열 확인
        linear = board[0][c] + board[1][c] + board[2][c]
        if linear == 'OOO':
            winner.append('O')
        elif linear == 'XXX':
            winner.append('X')
                
    asc_diagonal, desc_diagonal = '', ''
    for i in range(3): # 대각선 확인
        asc_diagonal += board[i][i]
        desc_diagonal += board[i][2-i]
        
    if asc_diagonal == 'OOO':
        winner.append('O')
    elif asc_diagonal == 'XXX':
        winner.append('X')
        
    if desc_diagonal == 'OOO':
        winner.append('O')
    elif desc_diagonal == 'XXX':
        winner.append('X')
            
    if len(set(winner)) > 1 or len(winner) > 2:
        return 0     
                                                     
    p1, p2 = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                p1 += 1
            elif board[i][j] == 'X':
                p2 += 1
                    
    if p1 - p2 > 1 or p2 > p1: # 2개 이상 차이 나거나 'X'의 개수가 더 많을 경우
        return 0
    
    if winner:
        # 게임이 끝나고도 계속했을 경우
        if (winner[0] == 'O' and p1 == p2) or winner[0] == 'X' and p1 != p2:
            return 0
    return 1
