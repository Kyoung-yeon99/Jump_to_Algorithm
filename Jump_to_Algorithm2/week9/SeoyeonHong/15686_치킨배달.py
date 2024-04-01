import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split()) # 도시의 크기, 유지할 치킨집 최대 개수
INF = int(1e9)
city_dist = INF # 도시의 치킨 거리, 초기값을 최댓값으로 설정
home = [] # 집
store = [] # 치킨집

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            home.append((r, c)) 
        elif row[c] == 2:
            store.append((r, c)) 

# 도시의 치킨 거리 계산
def calculate_dist(stores):
    total_dist = 0 # 각 집의 치킨 거리 합
    for hr, hc in home: # 각 집에 대해
        distance = INF
        for sr, sc in stores: # 각 가게에 대해
            distance = min(distance, abs(hr - sr) + abs(hc - sc)) # 치킨 거리 계산
        total_dist += distance # 총 치킨 거리에 최소 치킨 거리 추가
    return total_dist
    

for m in range(1, M+1): # 유지할 치킨집의 개수 m
    for combination in combinations(store, m): # m개의 치킨집의 조합
        city_dist = min(city_dist, calculate_dist(combination)) # 도시의 치킨거리 갱신

print(city_dist)
