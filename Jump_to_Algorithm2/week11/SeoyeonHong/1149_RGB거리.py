# 모든 집을 칠하는 비용의 최솟값
import sys
from collections import deque

input = sys.stdin.readline
N = int(input()) # 집의 수
house = []
max_cost = 1000 * N
dp = [[max_cost, max_cost, max_cost] for _ in range(N)]
min_cost = max_cost # 최소비용, 최댓값으로 초기화

for _ in range(N):
    house.append(list(map(int, input().split())))

q = deque([[0, 0, 0], [0, 1, 0], [0, 2, 0]])
while q:
    number, before, cost = q.popleft()
    if number == N: # 다 칠했을 경우
        min_cost = min(min_cost, cost)
    else:
        for cur in range(3):
            if cur != before: # 이전 집의 색과 다른 색만 고려
                new_cost = cost + house[number][cur]
                if new_cost < dp[number][cur]:
                    dp[number][cur] = new_cost
                    q.append((number+1, cur, new_cost))

print(min(dp[N-1]))