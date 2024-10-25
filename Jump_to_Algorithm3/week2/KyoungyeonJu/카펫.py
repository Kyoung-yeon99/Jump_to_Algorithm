import math


def solution(brown, yellow):
    # 갈색 격자 수 = 2h + 2w -4
    # 노란색 격자 수 = (h-2)*(w-2)= hw - 2h - 2w + 4

    add = (brown + 4) // 2
    multi = brown + yellow
    start = math.ceil(add / 2)

    for w in range(start, add):
        h = add - w
        if multi == w * h:
            return [w, h]
