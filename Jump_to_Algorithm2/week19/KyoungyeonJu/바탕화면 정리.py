def solution(wallpaper):
    # 가장 왼쪽에 위치한 luy 3 w[3][3]
    # 가장 위쪽에 위치한 lux 1 w[1][5]
    # 가장 오른쪽에 위치한 rdy 8 w[2][7]
    # 가장 아래쪽에 위치한 rdx 5 w[4][4]

    H, W = len(wallpaper), len(wallpaper[0])
    lux, luy = H, W
    rdx, rdy = -1, -1

    for i in range(H):
        row = list(wallpaper[i])
        for j in range(W):
            if row[j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i + 1)
                rdy = max(rdy, j + 1)
                print(f'lux = {lux} luy = {luy} rdx = {rdx} rdy = {rdy}')

    return [lux, luy, rdx, rdy]
