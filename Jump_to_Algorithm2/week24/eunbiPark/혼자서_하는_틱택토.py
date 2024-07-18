def solution(board):
    def won(player):
        # 가로 
        for i in range(3):
            if all(cell == player for cell in board[i]):
                return True
        
        # 세로 
        for j in range(3):
            if all(board[i][j] == player for i in range(3)):
                return True
        
        # 대각선 
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True
    
        return False 
    
    num_x, num_o = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                num_x += 1
            elif board[i][j] == 'O':
                num_o += 1
     
    if num_x > num_o or abs(num_x - num_o) > 1:
        return 0
    elif (won('O') and num_x != num_o - 1) or (won('X') and num_x != num_o):
        return 0

    return 1
