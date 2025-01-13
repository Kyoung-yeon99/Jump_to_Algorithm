import sys

input = sys.stdin.readline
N, M = map(int, input().split())
level = {}

for _ in range(N):
    title, power = input().split()
    power = int(power)
    if power not in level: # 중복되는 상한값을 가진 칭호가 있을 경우 사용X
        level[power] = title

level = sorted(level.items()) # 상한값 기준 오름차순으로 정렬

for _ in range(M):
    power = int(input()) # 캐릭터의 전투력
    start, end = 0, len(level)-1
    while start < end: # 이분탐색
        mid = (start + end) // 2        
        if level[mid][0] >= power:
            end = mid
        else:
            start = mid+1
    print(level[end][1]) # 캐릭터의 전투력에 맞는 칭호 출력


