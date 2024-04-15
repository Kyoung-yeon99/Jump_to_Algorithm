# https://velog.io/@highcho/Algorithm-baekjoon-1927

import heapq
import sys

# 연산의 개수
n = int(sys.stdin.readline())

# 숫자 저장할 리스트
arr = []

# 0: 배열에서 가장 작은 값 출력 & 배열에서 제거
for i in range(n):
    number = int(sys.stdin.readline())
    if number == 0:
        # 배열이 비어있을 경우 0 출력
        if len(arr) == 0:
            print(0)
            continue
        print(heapq.heappop(arr))
    else:  # 숫자라면 힙에 삽입
        heapq.heappush(arr, number)
