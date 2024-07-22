from collections import deque


def solution(maps):
    # 초기화
    n, m = len(maps), len(maps[0])
    start, lever, exit = None, None, None

    # 시작 지점(S), 레버(L), 출구(E) 위치 찾기
    for x in range(n):
        for y in range(m):
            if maps[x][y] == "S":
                start = (x, y)
            elif maps[x][y] == "E":
                exit = (x, y)
            elif maps[x][y] == "L":
                lever = (x, y)

    # BFS 함수 정의
    def bfs(start, target):
        sx, sy = start
        tx, ty = target
        q = deque([(sx, sy, 0)])
        visited = [[False] * m for _ in range(n)]
        visited[sx][sy] = True

        while q:
            x, y, level = q.popleft()

            # 목표 지점에 도달하면 이동 횟수 반환
            if x == tx and y == ty:
                return level

            # 상하좌우 방향 탐색
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X":
                    q.append((nx, ny, level + 1))
                    visited[nx][ny] = True

        return -1  # 목표 지점에 도달하지 못하면 -1 반환

    # 시작 지점에서 레버까지 이동
    to_lever = bfs(start, lever)
    if to_lever == -1:
        return -1

    # 레버에서 출구까지 이동
    to_exit = bfs(lever, exit)
    if to_exit == -1:
        return -1

    # 총 이동 횟수 반환
    return to_lever + to_exit