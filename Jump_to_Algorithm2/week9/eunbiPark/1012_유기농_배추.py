import sys
sys.setrecursionlimit(10**7)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if 0 > x or x >= m or 0 > y or y >= n:
        return False

    if board[x][y] == 1:
        board[x][y] = 0
        for r in range(4):
            nx, ny = x + dx[r], y + dy[r]
            dfs(nx, ny)
        return True # 한 칸 더 들여쓰면 안된다
    return False

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * n for _ in range(m)]
    for _ in range(k):
        a, b = map(int, input().split())
        board[a][b] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                cnt += 1
    print(cnt)