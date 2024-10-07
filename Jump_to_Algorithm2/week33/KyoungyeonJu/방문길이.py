def solution(dirs):
    d = {'U': [1, 0], 'D': [-1, 0], 'L': [0, -1], 'R': [0, 1]}
    lens = set()

    x, y = 0, 0
    for dir in dirs:
        r, c = d[dir]
        if -5 <= x + r <= 5 and -5 <= y + c <= 5:  # 범위 안에 들어오는지 확인
            nx, ny = x + r, y + c
            if dir == 'R' or dir == 'U':
                lens.add((x, y, nx, ny))
            elif dir == 'L' or dir == 'D':
                lens.add((nx, ny, x, y))
            x, y = nx, ny

    return len(lens)