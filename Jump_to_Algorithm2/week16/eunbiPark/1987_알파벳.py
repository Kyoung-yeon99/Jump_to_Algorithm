import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [
    list(map(lambda x: ord(x) - 65, input().strip()))
    for _ in range(r)
]

visited = [0] * 26
max_ = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt):
    global max_
    max_ = max(cnt, max_)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 확인
        if 0 <= nx < r and 0 <= ny < c:
            if not visited[board[nx][ny]]:
                visited[board[nx][ny]] = 1
                dfs(nx, ny, cnt + 1)
                visited[board[nx][ny]] = 0

# main
visited[board[0][0]] = True
dfs(0, 0, max_)
print(max_)