import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

ladder = {}
snake = {}

for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

# 1~6 사이에 사라리, 뱀 있으면 타기
def bfs():
    while q:
        x = q.popleft()
        if x == 100:
            print(visited[100] - 1)
            return
        for dx in [1, 2, 3, 4, 5, 6]:
            nx = x + dx
            if nx <= 100 and not visited[nx]:
                # 사다리, 뱀 이동 이동
                if nx in ladder:
                    nx = ladder[nx]
                if nx in snake:
                    nx = snake[nx]

                if not visited[nx]: # nx 의 값을 변경했기에 다시 한 번 방문확인
                    q.append(nx)
                    visited[nx] = visited[x] + 1


# main
q = deque()
q.append(1)
visited = [0 for _ in range(101)]
visited[1] = 1
bfs()