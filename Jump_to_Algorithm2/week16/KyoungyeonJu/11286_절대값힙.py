import sys
import heapq
input = sys.stdin.readline  # 없으면 시간초과

n = int(input())
h = []
for _ in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(h, (abs(a), a))
    else:
        if len(h) == 0:
            print(0)
        else:
            abs_num, num = heapq.heappop(h)
            print(num)

