from collections import deque

n, m = map(int, input().split())
# 2차원 정보의 미로
board = [input() for _ in range(n)]  # 문자열로 입력받음(공백 x)

# 길찾기 dxs, dys
dxs = (1, 0, -1, 0)
dys = (0, 1, 0, -1)


# 범위 체크
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


# 문제에서는 (1,1) 시작 => 인덱스 기준이므로 (0,0)에서 출발
def bfs():
    # 방문 체크용
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True  # 시작 위치 방문 처리
    q = deque()  # 큐 생성
    q.append((0, 0, 1))  # 시작 위치(0,0)과 지나야 하는 칸수(시작칸도 포함이므로 1부터 시작)

    while q:
        x, y, d = q.popleft()  # xy 위치, 이동해야하는 칸 수

        if x == n - 1 and y == m - 1:  # 도착위치 도달시
            return d

        nd = d + 1  # 한칸씩 증가
        for k in range(4):  # 4방탐색
            nx = x + dxs[k]
            ny = y + dys[k]
            # 체크할 조건이 여러개라면 무조건 "범위"부터 체크(index error 방지)
            # 범위 내이고, 방문하지 않았으며, 1일 경우(이동할 수 있는 칸)
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == '1':
                visited[nx][ny] = True  # 방문 처리
                q.append((nx, ny, nd))  # 큐에 삽입


# 출력
print(bfs())
