def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])

    files = [
        (i, j)
        for i in range(n)
        for j in range(m)
        if wallpaper[i][j] == '#'
    ]

    files.sort(key=lambda x: x[0])
    sx = files[0][0]
    ex = files[-1][0] + 1  # 우하단까지 드래그

    files.sort(key=lambda x: x[1])
    sy = files[0][1]
    ey = files[-1][1] + 1  # 우하단까지 드래그

    return [sx, sy, ex, ey]


'''
# sol2) x, y 배열을 만들어 min, max 활용
a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]

'''