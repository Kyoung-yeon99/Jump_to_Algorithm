# 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램
import sys

input = sys.stdin.readline
N, C = map(int, input().split())
house = [] # 집들의 좌표
for _ in range(N):
    house.append(int(input()))

house.sort() # 오름차순 정렬

l = 1
r = house[-1] - house[0]
answer = 0

while l <= r:
    min_dist = (l + r) // 2 # 가장 인접한 두 공유기 사이의 거리
    count = 1 # 공유기 개수
    last_router = house[0]
    
    for i in range(1, N):
        if house[i] - last_router >= min_dist:
            last_router = house[i]
            count += 1
    
    if count >= C:
        l = min_dist + 1
    else:
        r = min_dist - 1

print(r)



