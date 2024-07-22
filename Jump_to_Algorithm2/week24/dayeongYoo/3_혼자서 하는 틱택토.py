def solution(board):
    # 1. 개수상의 모순이 있는가?
    O_count, X_count = 0, 0
    for row in board:
        for cell in row:
            if cell == 'O':
                O_count += 1
            elif cell == 'X':
                X_count += 1

    # O는 X보다 1개 많거나 같아야 한다
    if O_count - X_count not in [0, 1]:
        return 0

    # 2. 규칙상의 모순이 있는가?
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 하, 우, 대각선 하우, 대각선 하좌
    results = []

    def dfs(x, y, player, direction, depth):
        if depth == 3:
            if player == 'O':
                if O_count != X_count + 1:
                    results.append(0)
                else:
                    results.append(1)
            elif player == 'X':
                if X_count != O_count:
                    results.append(0)
                else:
                    results.append(2)
            return

        if depth == 1:  # 첫 탐색 시 모든 방향 탐색
            for d, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < 3 and 0 <= ny < 3 and board[nx][ny] == player:
                    dfs(nx, ny, player, d, depth + 1)
        else:  # 두번째 이상의 탐색 시 주어진 방향으로만 탐색
            dx, dy = directions[direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3 and board[nx][ny] == player:
                dfs(nx, ny, player, direction, depth + 1)

    # DFS 실행
    for r in range(3):
        for c in range(3):
            if board[r][c] != '.':
                dfs(r, c, board[r][c], -1, 1)

    # 3. 우승자의 모순이 있는가?
    if 1 in results and 2 in results:
        return 0
    if 0 in results:
        return 0
    return 1
