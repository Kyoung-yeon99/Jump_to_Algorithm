# 최소 . 가장 멀리 있는 개미 중 가까운 끝까지 걸리는 시간
# 최대 . 가장 끝에 있는 개미 중 반대 까지 걸리는 시간

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    l, n = map(int, sys.stdin.readline().split())

    _min, _max = 0, 0
    ants = []
    for _ in range(n):
        i = int(sys.stdin.readline())

        straight = min(i, l - i)
        _min = max(_min, straight)

        _max = max(_max, i, l - i)

    print(_min, _max)




# 시간초과 