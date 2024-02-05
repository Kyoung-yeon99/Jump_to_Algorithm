# 방의 크기 n,m
n, m = map(int, input().split())

# 로봇청소기 좌표, 방향
r, c, d = map(int, input().split())
# 2차원 배열
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 정답
ans = 0


def dfs(x, y, d):
    global ans
    # 현재 칸이 청소안되었다면, 현재 칸 청소
    if board[x][y] == 0:
        board[x][y] = -1  # 청소
        ans += 1
    for i in range(4):
        nd = (d + 3) % 4  # 반시계 회전
        nx = x + dx[nd]
        ny = y + dy[nd]
        if board[nx][ny] == 0:  # 청소 가능
            dfs(nx, ny, nd)  # 탐색 시작
            return
        d = nd
    # 뒤쪽 칸
    bd = (d + 2) % 4
    nx = x + dx[bd]  # 한칸 후진
    ny = y + dy[bd]

    if board[nx][ny] == 1:  # 벽이라면
        return  # 작동 stop
    dfs(nx, ny, d)  # 바라보는 방향 유지한채 한칸 후진


dfs(r, c, d)
print(ans)
