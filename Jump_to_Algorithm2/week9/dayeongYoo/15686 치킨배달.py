# 최소 치킨 거리 구하기

import sys
from itertools import combinations

INF = float('inf')  # 최소값 비교

# 입력값 받기
# n: 도시 크기, m: 치킨집 개수
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

# 0: 빈칸, 1: 집, 2: 치킨집
house = []
chicken = []
answer = INF

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:  # 집이라면
            house.append((i, j))  # 집 리스트에 추가
        elif city[i][j] == 2:  # 치킨집이라면
            chicken.append(((i, j)))  # 치킨집 리스트에 추가

# 최대 m개의 치킨집 고를 수 있음
# 선택된 치킨집이 많으면 많을 수록 거리 최소가 될 가능성 높음
# 전체 치킨집 중 m개 선택하되(조합), 그중에서 거리가 가장 최소가 되는 곳으로 갱신해 나가기->완탐


for x in combinations(chicken, m):

    total_dist = 0

    for r1, c1 in house:  # 집과
        house_dist = INF  # 거리 초기화
        for r2, c2 in x:  # 치킨집 사이 거리
            house_dist = min(house_dist, abs(r1 - r2) + abs(c1 - c2))  # 치킨 거리
        total_dist += house_dist

    answer = min(answer, total_dist)

print(answer)
