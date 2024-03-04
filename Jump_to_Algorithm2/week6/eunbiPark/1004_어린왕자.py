# sx, sy, ex, ey를 포함하는 원의 수
import math
def in_range(x, y, r):
    # r > sqrt(((sx, sy) 혹은 (ex, ey)) ~ (x, y))
    # 거리 계산
    start = math.sqrt((sx - x) ** 2 + (sy - y) ** 2)
    end = math.sqrt((ex - x) ** 2 + (ey - y) ** 2)
    # 한 원에 둘 다 포함되는 경우 - 0 반환
    if r > start and r > end:
        return 0
    # 일반적인 경우 - 겹친 원의 개수 반환
    return r > start or r > end

t = int(input())

for _ in range(t):
    cnt = 0
    sx, sy, ex, ey = map(int, input().split())
    n = int(input())
    planet = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    for x, y, r in planet:
        cnt += in_range(x, y, r)

    print(cnt)