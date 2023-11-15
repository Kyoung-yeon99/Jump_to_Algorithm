import sys
from collections import deque
input = sys.stdin.readline

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    # 선언
    q = deque()
    # 초기화
    q.append(n)
    # 반복
    while q:
        x = q.popleft()
        # 정답 조건
        if x == k:
            print(dist[x])
            path(x)
            break

        for j in (x-1, x+1, x*2):
            if 0 <= j <= MAX and not dist[j]:
                dist[j] = dist[x] + 1
                move[j] = x
                q.append(j)

MAX = 1000000
n, k = map(int, input().split())
dist = [0] * (MAX + 1)
move = [0] * (MAX + 1)

bfs()