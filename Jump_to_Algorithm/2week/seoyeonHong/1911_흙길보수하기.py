import math
n, l = map(int, input().split()) # 정수 N과 L
count = 0 # 널빤지의 개수
load = []

for i in range(n):
    start, end = map(int, input().split()) # 웅덩이의 시작 위치와 끝 위치
    load.append((start, end)) # 웅덩이 위치 저장
    load.sort() # 오름차순 정렬

plankPosition = 0 # 널빤지 끝의 위치

for (start, end) in load: # 웅덩이마다 널빤지 덮기
    if plankPosition > start : # 이전 널빤지가 현재 웅덩이의 일부분을 덮었을 경우
        start = plankPosition # 웅덩이의 범위에서 널빤지가 덮고 있는 부분 제외

    length = end - start # 웅덩이의 길이
    count += math.ceil(length / l) # 웅덩이를 덮기 위해 필요한 널빤지의 개수 더하기
    
    if length % l == 0: # 널빤지 끝의 위치 계산
        plankPosition = end
    else:
        plankPosition = end + l - length % l

print(count)
