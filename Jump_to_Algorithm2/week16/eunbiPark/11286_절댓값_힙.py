import sys
import heapq
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(plus, x)
    elif x < 0:
        heapq.heappush(minus, -x) # -1, -2, -3 ...
    else:
        if len(plus) and len(minus):
            if plus[0] > minus[0]:
                print(-heapq.heappop(minus))
            elif plus[0] < minus[0]:
                print(heapq.heappop(plus))
            else:
                print(-heapq.heappop(minus))
        elif len(plus) and not len(minus):
            print(heapq.heappop(plus))
        elif not len(plus) and len(minus):
            print(-heapq.heappop(minus))
        else:
            print(0)