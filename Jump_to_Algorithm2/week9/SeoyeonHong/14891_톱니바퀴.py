import sys
from collections import deque

input = sys.stdin.readline
gear = [] # 톱니바퀴 정보
for i in range(4):
    nums = deque(input())
    nums.pop() # '\n' 제거
    gear.append(nums)
score = 0 # 점수
k = int(input()) # 회전 횟수

for _ in range(k): # k번 회전
    num, dir = map(int, input().split()) # 회전시킨 톱니바퀴 번호, 회전 방향
    num -= 1 # 인덱스와 톱니바퀴 번호의 차이 없애기
    direction = [0, 0, 0, 0] # 각 톱니바퀴의 회전 방향, 1: 시계방향, -1: 반시계방향, 0: 회전X
    direction[num] = dir

    for i in range(1, 4): # 4개의 톱니바퀴에 대해
        # 같은 극이 접하고 있으면 회전하지X, 다른 극이 맞다으면 반대방향으로 회전
        if num + i < 4:
            d = gear[num+i-1][2] == gear[num+i][6] # 같은 극이면 True, 다른 극이면 False
            if d:
                d = 0
            else:
                d = -1
            direction[num+i] = direction[num+i-1] * d
        if num - i >= 0:
            d = gear[num - i][2] == gear[num-i+1][6]
            if d:
                d = 0
            else:
                d = -1
            direction[num-i] = direction[num-i+1] * d

    for i in range(4):
        gear[i].rotate(direction[i])
    
for i in range(4): # 점수 계산
    if gear[i][0] == '1':
        score += 2 ** i
    
print(score)


