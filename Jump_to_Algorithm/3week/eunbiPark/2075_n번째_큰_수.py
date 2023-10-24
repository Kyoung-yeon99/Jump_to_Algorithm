import heapq
n = int(input())

# heap에 n개 만 넣으며 비교
heap = []
for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap,num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])