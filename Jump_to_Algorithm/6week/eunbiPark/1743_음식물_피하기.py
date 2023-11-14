import sys
sys.setrecursionlimit(10**5)
n, m, k = map(int, input().split())

board = [
    [0] * m
    for _ in range(n)
]

for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count = 0
def dfs(x, y):
    global count

    # 예외 처리
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if board[x][y] == 1:
        count += 1
        board[x][y] = 2
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

ret = []
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            ret.append(count)
            count = 0

print(max(ret))