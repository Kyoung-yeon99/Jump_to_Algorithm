import sys
import heapq

input = sys.stdin.readline
heap = []
N = int(input()) # 연산의 개수
for _ in range(N):
    x = int(input())
    if x > 0: # x가 자연수라면
        heapq.heappush(heap, x) # 배열에 x 추가
        
    else: # x가 0이라면
        if len(heap) == 0: # 힙이 비었을 경우
            print(0)
        else:
            print(heapq.heappop(heap)) # 가장 작은 값 출력
        
