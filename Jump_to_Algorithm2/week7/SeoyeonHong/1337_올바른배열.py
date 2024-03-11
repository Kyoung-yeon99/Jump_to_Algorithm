import sys
import heapq

input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

pq = []

for i in range(N):
    n = arr[i]
    cnt = 1
    for j in range(n+1, n+5): # i ~ i+5 사이 숫자의 개수
        if j in arr:
            cnt += 1
    heapq.heappush(pq, -cnt)
    if cnt >= 5: # 이미 올바른 배열일 경우 0 출력
        print(0)
        exit()

print(5 + heapq.heappop(pq))