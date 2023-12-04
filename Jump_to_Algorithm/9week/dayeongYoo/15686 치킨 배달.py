# 최소 치킨 거리 구하기

import sys
from itertools import combinations

INF = 2147000000  # 최소값 비교

# 입력값 받기
# n: 도시 크기, m: 치킨집 개수
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

# print(n, m)
# for i in range(n):
#     print(city[i])

# 0: 빈칸, 1: 집, 2: 치킨집
house = []
chicken = []
answer = INF

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append(((i, j)))

# 최대 m개의 치킨집 고를 수 있음
# 선택된 치킨집이 많으면 많을 수록 거리 최소가 될 가능성 높음
# 전체 치킨집 중 m개 선택하되, 그중에서 거리가 가장 최소가 되는 곳고르기.

for x in combinations(chicken, m):
    total_distance = 0
    for r1, c1 in house:
        house_distance = INF
        for r2, c2 in x:
            house_distance = min(house_distance, abs(r1 - r2) + abs(c1 - c2))
        total_distance += house_distance

    answer = min(answer, total_distance)

print(answer)
