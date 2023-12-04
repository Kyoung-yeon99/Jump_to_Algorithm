import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = [
    list(map(int, input().split()))
    for _ in range(n)
    ]
ret = 1e9
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

for c in combinations(chicken, m):
    temp = 0
    for h in house:
        chicken_distance = 1e9
        for j in range(m):
            chicken_distance = min(chicken_distance, abs(h[0] - c[j][0]) + abs(h[1] - c[j][1]))
        temp += chicken_distance
    ret = min(ret, temp)

print(ret)