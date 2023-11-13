from collections import deque

n, m = map(int, input().split())
# 2차원 정보의 미로
board = [input() for _ in range(n)]

dxs = (1, 0, -1, 0)
dys = (0, 1, 0, -1)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


# (1,1) 시작 => 인덱스에서는 (0,0)에서 출발
def bfs():
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque()
    q.append((0, 0, 1))  # 시작 위치(0,0)과 지나야 하는 칸수(시작칸도 포함이므로 1부터 시작)

    while q:
        x, y, d = q.popleft()

        if x == n - 1 and y == m - 1:  # 도착위치 도달시
            return d

        nd = d + 1  # 한칸씩 증가
        for k in range(4):
            nx = x + dxs[k]
            ny = y + dys[k]
            # 체크할 조건이 여러개라면 무조건 "범위"부터 체크(index error 방지)
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == '1':
                visited[nx][ny] = True
                q.append((nx, ny, nd))


# 출력
print(bfs())
