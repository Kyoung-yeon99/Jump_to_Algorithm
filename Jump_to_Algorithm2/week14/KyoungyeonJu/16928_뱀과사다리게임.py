from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ladders, snakes = {}, {}

for _ in range(n):
    s, e = map(int, input().split())
    ladders[s] = e

for _ in range(m):
    s, e = map(int, input().split())
    snakes[s] = e

visited = [0]*(100+1)
visited[1] = 1
cnt = int(2e9)
q = deque()
q.append((1, 0))  # 위치, 주사위 굴린 수
while q:
    x, dice = q.popleft()

    if x >= 100:
        cnt = min(cnt, dice)
        continue

    for i in range(1, 7):  # 1부터 6까지 주사위 굴리기
        if x + i < 100 and not visited[x+i]:
            if x+i in ladders:
                q.append((min(100, ladders[x+i]), dice+1))
            elif x+i in snakes:
                q.append((min(100, snakes[x+i]), dice+1))
            else:
                q.append((min(100, x+i), dice+1))
            visited[x+i] = 1
        elif x + i >= 100:
            q.append((100, dice+1))
            visited[100] = 1

print(cnt)