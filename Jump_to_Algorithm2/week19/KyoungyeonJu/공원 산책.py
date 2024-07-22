def solution(park, routes):
    H, W = len(park), len(park[1])
    obstacle = {}  # 장애물 위치 딕셔너리
    d = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    pos = [-1, -1]  # 시작 위치
    con1, con2 = True, True  # 두 가지 조건 만족 확인 FLAG

    # 시작 위치, 장애물 위치 파악
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'O':
                continue
            elif park[i][j] == 'X':
                obstacle[(i, j)] = (i, j)
            elif park[i][j] == 'S':
                pos[0], pos[1] = i, j


    # 이동하기
    for r in routes:
        direction, step = r.split()
        step = int(step)
        r, c = d[direction]

        tmp = [pos[0], pos[1]]  # tmp = pos 는 call by reference

        for i in range(step):
            nr, nc = pos[0] + r, pos[1] + c
            if 0 <= nr < H and 0 <= nc < W:  # 조건 1. 공원 벗어나지 않는지 확인
                if (nr, nc) not in obstacle:  # 조건 2. 해당 위치에 장애물이 없는지 확인
                    pos[0], pos[1] = nr, nc
                else:
                    con2 = False
                    break
            else:
                con1 = False
                break

        if not con1 or not con2:
            pos = tmp
            con1, con2 = True, True    

    return list(pos)