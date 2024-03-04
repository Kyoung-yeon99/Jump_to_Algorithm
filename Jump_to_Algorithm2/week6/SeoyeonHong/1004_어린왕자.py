# 어린 왕자가 거쳐야 할 최소의 행성계 진입/이탈 횟수
import sys

input = sys.stdin.readline
T = int(input()) # 테스트 케이스 개수
for _ in range(T):
    x1, y1, x2, y2  = map(int, input().split()) # 출발점과 도착점
    n = int(input()) # 행성계의 개수
    cnt = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split()) # 행성계의 중점과 반지름
    
        if pow(cx-x1, 2) + pow(cy-y1, 2) < pow(r, 2):
            if pow(cx-x2, 2) + pow(cy-y2, 2) < pow(r, 2): # 출발점과 도착점이 모두 포함될 경우
                continue
            else: # 출발점만 포함될 경우
                cnt += 1
        elif pow(cx-x2, 2) + pow(cy-y2, 2) < pow(r, 2): # 도착점만 포함될 경우
            cnt += 1

    print(cnt)