# 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값
from collections import deque

N, M = map(int, input().split()) # 사다리와 뱀의 수
ladder = [-1 for _ in range(101)] # 사다리, x -> y
snake = [-1 for _ in range(101)] # 뱀, u -> v
INF = int(1e9)
dp = {i: INF for i in range(1, 101)}

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

q = deque([[1, 0]])

while q:
    i, cnt = q.popleft()
    if i == 100: # 도착했을 경우 종료
        print(cnt)
        break

    cnt += 1
    for j in range(i+1, min(101, i+7)): # 각 주사위 숫자가 나온 경우에 대해
        if ladder[j] > 0: # 사다리가 있는 칸이면
            if dp[j] > cnt: # 현재 칸까지 주사위를 최소한으로 굴려서 도착한 경우라면
                dp[j] = cnt
                q.append([ladder[j], cnt])
        elif snake[j] > 0: # 뱀이 있는 칸이면
            if dp[j] > cnt:
                dp[j] = cnt
                q.append([snake[j], cnt])
        else: # 아무것도 없는 칸이면
            if dp[j] > cnt:
                dp[j] = cnt
                q.append([j, cnt])
