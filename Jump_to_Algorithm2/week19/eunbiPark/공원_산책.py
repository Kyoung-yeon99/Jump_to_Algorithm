def solution(park, routes):
    m = len(park[0])
    n = len(park)
    dr = {'N': 0, 'S': 1, 'W': 2, 'E': 3}
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]  # 북남서동

    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x, y = i, j
                break

    def in_range(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return True

    def can_go(x, y):
        # park[x][y] 먼저 확인하면 인덱스 오류 가능
        if not in_range(x, y) or park[x][y] == 'X':
            return False
        return True

    for route in routes:
        # 이동 정보 등록
        d = dr[route[0]]
        move = int(route[2])

        # 이동 - 이동중 장애물, 범위 확인 -> 하나씩 이동
        tx, ty = x, y
        for _ in range(move):
            nx, ny = tx + dxs[d], ty + dys[d]
            if can_go(nx, ny):
                tx, ty = nx, ny
            else:
                tx, ty = x, y
                break

        x, y = tx, ty

    return [x, y]