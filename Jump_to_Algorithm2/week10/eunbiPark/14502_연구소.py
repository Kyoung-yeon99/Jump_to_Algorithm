# 0: 빈 칸, 1: 방화벽, 2: 불
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

fires = [
    (i, j)
    for i in range(n)
    for j in range(m)
    if board[i][j] == 2
]

none = [
    (i, j)
    for i in range(n)
    for j in range(m)
    if board[i][j] == 0
]

walls_cnt = 3
walls_cnt += sum(
    board[i][j]
    for i in range(n)
    for j in range(m)
    if board[i][j] == 1
)


def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    return True


def bfs(q, temp_board, visited):
    while q:
        x, y = q.popleft()
        # print(x, y)
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and temp_board[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1


def calc(visited):
    temp = sum(
        1
        for i in range(n)
        for j in range(m)
        if visited[i][j] == 0
    )
    return temp


# 방화벽 설치하고 불 bfs 돌리기
def simulation(choose):
    # board 복사
    temp_board = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp_board[i][j] = board[i][j]

            # 방화벽 추가 설치
    for c in choose:
        temp_board[c[0]][c[1]] = 1

    # 초기 작업
    q = deque()
    visited = [[0] * m for _ in range(n)]
    for f in fires:
        # 큐 초깃값
        q.append(f)
        # 방문 처리  - 나중에 해야 하는지 잘 보기, 벽도 해야 하는지 확인
        visited[f[0]][f[1]] = 1

    bfs(q, temp_board, visited)

    # 남은 공간 세기
    return calc(visited)


########## main
ans = 0

# 방화벽 3개 고르기
choose = []


def choice(num):
    global ans
    if num == 3:
        ans = max(simulation(choose), ans)
        return

    for no in none:
        if no not in choose:
            choose.append(no)
            choice(num + 1)
            choose.pop()


choice(0)

print(ans - walls_cnt)