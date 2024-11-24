# 최소 주사위를 굴려야 하는 횟수의 최솟값
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [-1]*101
visited = [False]*101
for _ in range(n+m):
    a, b = map(int, input().split())
    maps[a] = b

q = deque()
q.append((1, 0))
visited[1] = True

while q:
    idx, cnt = q.popleft()
    if idx == 100:
        print(cnt)
        exit(0)
    for i in range(1, 7):
        next_idx = idx + i
        if next_idx <= 100 and not visited[next_idx]:
            if maps[next_idx] != -1:  # 사다리 또는 뱀
                visited[maps[next_idx]] = True  # visited[next_idx] 없어도 통과
                q.append((maps[next_idx], cnt+1))
            else:
                visited[next_idx] = True
                q.append((next_idx, cnt+1))




