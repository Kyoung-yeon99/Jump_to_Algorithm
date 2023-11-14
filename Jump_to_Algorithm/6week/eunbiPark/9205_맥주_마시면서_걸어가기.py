import sys
from collections import deque
input = sys.stdin.readline


def bfs(sx, sy, px, py, combine):
    checker = deque()
    q = deque()
    checker.append([sx, sy])
    q.append([sx, sy])

    while q:
        cx, cy = q.popleft()
        if abs(cx - px) + abs(cy - py) <= 1000:
            return "happy"
        for i in range(len(combine)):
            if not [combine[i][0], combine[i][1]] in checker and abs(cx - combine[i][0]) + abs(cy - combine[i][1]) <= 1000:
                checker.append([combine[i][0], combine[i][1]])
                q.append([combine[i][0], combine[i][1]])
    return "sad"

t = int(input())
for _ in range(t):
    combine = [] # 편의점 좌표
    n = int(input()) # 편의점 개수
    sx, sy = map(int, input().split()) # 상근이네 집
    for i in range(n):
        combine.append(list(map(int, input().split()))) # 편의점
    px, py = map(int, input().split()) # 펜타포트

    print(bfs(sx, sy, px, py, combine))
