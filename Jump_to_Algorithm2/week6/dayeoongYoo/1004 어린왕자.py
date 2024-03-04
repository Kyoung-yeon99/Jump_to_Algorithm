# 출발점 ~ 도착점.
# 최소로 이탈하도록.

import math

t = int(input())

for _ in range(t):  # 테스트 케이스
    # 출발점(x1, y1)과 도착점(x2, y2)
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input())  # 행성계 개수
    ans = 0  # 원을 지나는 개수

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        # 거리 계산
        start_to_mid = math.sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        fin_to_mid = math.sqrt((x2 - cx) ** 2 + (y2 - cy) ** 2)
        # 행성계 내부의 점
        # 출발점
        if start_to_mid < r and fin_to_mid < r:  # 둘다 안에 있을 경우 행성계를 안지나가도 됨.
            pass
        elif start_to_mid < r:
            ans += 1
        elif fin_to_mid < r:
            ans += 1
    print(ans)
