def solution(board, h, w):
    def in_range(x, y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        return True

    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    color = board[h][w]
    ret = 0
    n = len(board)

    for dx, dy in zip(dxs, dys):
        nx, ny = dx + h, dy + w
        if in_range(nx, ny) and board[nx][ny] == color:
            ret += 1

    return ret