import heapq
from sys import stdin
N = int(stdin.readline().rstrip())
h = []
for _ in range(N):
    input = int(stdin.readline().rstrip())
    if input == 0:
        if h:
            #가장 작은 값 출력, 제거
            pop = heapq.heappop(h)
            print(pop)
        else:
            print(0)
    else:
        heapq.heappush(h,input)
