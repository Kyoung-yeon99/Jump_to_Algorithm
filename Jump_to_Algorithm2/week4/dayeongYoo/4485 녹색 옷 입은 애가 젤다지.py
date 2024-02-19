# 오른쪽 아래까지 최소 금액만 잃도록
# 상하좌우 1칸씩 이동
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 최단거리 이므로 bfs 수행.
ans = 0


def bfs():
    # 첫번째 칸에서 시작
    visited[0][0] = board[0][0]
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 1. 범위체크
            if not in_range(nx, ny):
                continue
            # 2. 해당 칸이 첫방문이라면
            if visited[nx][ny] == -1:
                # 최솟값 갱신
                visited[nx][ny] = visited[x][y] + board[nx][ny]
                q.append((nx, ny))  # 큐에 삽입
            # 2-1. 그렇지 않고 이미 방문한 칸이라면, 만약 최솟값으로 갱신 가능할 때만 큐에 삽입.
            elif visited[nx][ny] > -1:
                if visited[nx][ny] > visited[x][y] + board[nx][ny]:
                    visited[nx][ny] = visited[x][y] + board[nx][ny]
                    q.append((nx, ny))

    return visited[n - 1][n - 1]


tc = 0

while (True):
    # 맵 크기
    n = int(input())
    if n == 0:
        break

    board = [list(map(int, input().split())) for _ in range(n)]

    # 방문체크용
    visited = [[-1] * n for _ in range(n)]

    ans = bfs()
    tc += 1
    print(f'Problem {tc}: {ans}')
