import sys
import heapq

input = sys.stdin.readline
N = int(input()) # 연산의 개수
arr = []
heapq.heapify(arr)
for _ in range(N):
    x = int(input())
    if x == 0: # 0일 경우
        if arr: # 배열이 비지 않았다면
            print(heapq.heappop(arr)) # 가장 작은 값 출력&제거
        else: # 배열이 비었다면
            print(0)
    else: # 자연수일 경우
        heapq.heappush(arr, x) # 배열에 x 추가
