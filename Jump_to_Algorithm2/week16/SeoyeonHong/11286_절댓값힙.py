import heapq
import sys

input = sys.stdin.readline
N = int(input()) # 연산의 개수
count = 0
heap = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x)) # 배열에 x push
        count += 1
    else:
        if count == 0: # 배열이 비어 있는 경우
            print(0)
        else: # 절댓값이 가장 작은 값 pop
            a, n = heapq.heappop(heap)
            print(n)
            count -= 1
            
