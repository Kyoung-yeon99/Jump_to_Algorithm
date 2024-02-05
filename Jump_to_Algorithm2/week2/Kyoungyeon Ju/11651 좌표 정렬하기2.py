import heapq
n = int(input())
h = []

for i in range(n):
    x, y = map(int, input().split())
    heapq.heappush(h, [y, x])  # heapq로 우선순위큐 구현

for _ in range(n):
    y, x = heapq.heappop(h)
    print(x, y)
