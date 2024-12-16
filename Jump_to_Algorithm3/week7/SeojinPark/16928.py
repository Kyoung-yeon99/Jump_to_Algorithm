from collections import deque

n, m = map(int, input().split())
ladder={}
snake={}
board = [0]*101
visited=[False]*101

for _ in range(n):
    x, y=map(int, input().split())
    ladder[x] = y
for _ in range(m):
    x, y=map(int, input().split())
    snake[x] = y

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in range(1, 7):
            next = v+i
            if 0<next<=100 and not visited[next]:
                if next in ladder:
                    next=ladder[next]
                if next in snake:
                    next = snake[next]
                if not visited[next]:
                    queue.append(next)
                    visited[next] = True
                    board[next] = board[v]+1

bfs(1)
print(board[100])
