from collections import deque
n, m = map(int, input().split())

board = [
    list(map(int, input()))
    for _ in range(n)
]



dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 최소 칸의 개수 -> bfs
def bfs(x, y):
    # 생성, 초기화
    q = deque()
    q.append((x, y))

    # 반복
    while q:
        x, y = q.popleft()

        # 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 조건
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 0:
                continue

            # 이동
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

    return board[n-1][m-1]

# main
print(bfs(0, 0))