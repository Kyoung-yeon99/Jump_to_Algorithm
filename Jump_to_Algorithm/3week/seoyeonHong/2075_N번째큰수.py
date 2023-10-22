import sys
import heapq

n = int(sys.stdin.readline())
hq = []

for num in map(int, sys.stdin.readline().split()):
    heapq.heappush(hq, num)

for _ in range(n-1):
    for num in map(int, sys.stdin.readline().split()):
        if(hq[0] < num):
            heapq.heappop(hq)
            heapq.heappush(hq, num)

print(hq)
print(hq[0])    



# from queue import PriorityQueue
# line = []
# q = PriorityQueue(n*n)

# for i in range(n):
#     line = map(int, sys.stdin.readline().split())
#     for l in line:
#         q.put(-l)

# for i in range(n-1):
#     q.get()
# print(-q.get())