import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())

jewel = [] # 각 보석의 무게와 가격
for _ in range(N):
    jewel.append(list(map(int, input().split())))

bag = [] # 각 가방에 담을 수 있는 최대 무게
for _ in range(K):
    bag.append(int(input()))

jewel.sort() # 오름차순 정렬
bag.sort() # 오름차순 정렬 

cost = 0 # 담을 수 있는 보석 가격의 합
q = [] # 담을 수 있는 보석들(우선순위 큐)
j = 0 # 보석 인덱스

for b in bag:
    while j < N and jewel[j][0] <= b: # 담을 수 있는 보석이면
        heapq.heappush(q, -jewel[j][1])
        j += 1
    
    if q: # 담을 수 있는 보석이 있으면
        cost -= heapq.heappop(q)
    
print(cost)
