import heapq
import itertools

n = int(input())
heap = []
first_numbers = list(map(int, input().split()))  # 첫줄
for num in first_numbers:  # 리스트객체를 unpacking
    heapq.heappush(heap, num)  # heap에 넣어준다.

for i in range(n - 1):
    numbers = list(map(int, input().split()))  # 두번째 줄부터
    for num in numbers:
        if heap[0] < num:
            heapq.heappush(heap, num)  # 힙 오른쪽에 추가
            heapq.heappop(heap)  # 힙 왼쪽 요소 추출
print(heap[0])
