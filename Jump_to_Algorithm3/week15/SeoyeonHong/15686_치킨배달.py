import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
house = [] # 집의 위치
chicken = [] # 치킨 가게의 위치
min_distance = int(1e9) # 도시의 치킨 거리의 최솟값

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            house.append((r, c))
        elif row[c] == 2:
            chicken.append((r, c))

def calculate_distance(h, c): # 치킨 거리 계산
    chicken_distance = int(1e9)
    for i in range(len(c)):
        chicken_distance = min(chicken_distance, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
    return chicken_distance

for open in combinations(chicken, M): # M개의 치킨집을 고른 경우에 대해
    total_distance = 0
    for h in house:
        total_distance += calculate_distance(h, open)
    min_distance = min(min_distance, total_distance) # 도시의 치킨 거리의 최솟값 갱신

print(min_distance)
