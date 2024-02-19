# 개미가 모두 땅으로 떨어지는 가능한 시간 중 가장 빠른 시간, 느린 시간
# 두 개미가 만나 방향을 바꾸어 가도 걸리는 시간은 같으므로 무시
import sys
import heapq

input = sys.stdin.readline

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    L, N = map(int, input().split()) # 막대의 길이, 개미의 수
    mint = []
    maxt = []

    for _ in range(N):
        p = int(input())
        st = min(p, L-p) # 가까운 쪽으로 가는데 걸리는 시간
        lt = L - st # 먼 쪽으로 가는데 걸리는 시간
        heapq.heappush(mint, -st)
        heapq.heappush(maxt, -lt)
        
    print(-heapq.heappop(mint), -heapq.heappop(maxt)) # 가장 빠른 시간, 가장 느린 시간 출력