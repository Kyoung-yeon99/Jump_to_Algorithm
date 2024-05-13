def makeZ(x, y, w):
    global num
    if w == 2:
        if x <= r < x+w and y <= c < y+w:
            for i in range(x, x+2):
                for j in range(y, y+2):
                    if i == r and j == c:
                        print(num+1)
                        exit()
                    num += 1
    else:
        w = w//2
        # 왼위
        if (x <= r < x+w) and (y <= c < y+w):
            makeZ(x, y, w)
        else:
            num = num + w*w

        # 오위
        if (x <= r < x+w) and (y+w <= c < y+w+w):
            makeZ(x, y+w, w)
        else:
            num = num + w * w

        # 왼아래
        if (x+w <= r < x+w+w) and (y <= c < y+w):
            makeZ(x+w, y, w)
        else:
            num = num + w * w

        # 오아래
        if (x+w<=r<x+w+w) and (y+w<=c<y+w+w):
            makeZ(x+w, y+w, w)
        else:
            num = num + w * w


n, r, c = map(int, input().split())
lens = 2**n
num = -1
makeZ(0, 0, lens)

