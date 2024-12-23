import sys

input = sys.stdin.readline
N = int(input().rstrip()) # 기둥의 개수
pillar = []
max_height, max_idx = 0, 0 # 가장 높은 첫번쨰 기둥의 높이와 위치
for _ in range(N):
    L, H = map(int, input().split()) # 기둥의 위치, 높이
    pillar.append((L, H))

pillar = sorted(pillar, key=lambda x: x[0])

for i in range(N):
    if pillar[i][1] > max_height:
        max_height = pillar[i][1]
        max_idx = i

area = max_height # 창고 다각형의 면적, 가장 높은 기둥의 면적으로 초기화
h = pillar[0][1] # 현재 지붕의 높이

for i in range(1, max_idx+1): # 가장 높은 기둥의 오른쪽 면적 계산
    area += h * (pillar[i][0] - pillar[i-1][0])
    if pillar[i][1] > h: # 기둥의 높이가 더 높을 경우 지붕의 높이 갱신
        h = pillar[i][1]

h = pillar[-1][1]
for i in range(N-1, max_idx, -1): # 가장 높은 기둥의 왼쪽 면적 계산
    area += h * (pillar[i][0] - pillar[i-1][0])
    if pillar[i-1][1] > h: # 기둥의 높이가 더 높을 경우 지붕의 높이 갱신
        h = pillar[i-1][1]
    
print(area)