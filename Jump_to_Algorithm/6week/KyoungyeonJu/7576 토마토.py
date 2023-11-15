from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
tomato = []
qu = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    tomato.append(list(map(int, input().split())))

# 시작점이 여러 개, 즉 익은 사과의 시작 위치를 모두 큐 삽입
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            qu.append((i, j))

while qu:
    a, b = qu.popleft()
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[a][b] + 1
            qu.append((nx, ny))
            """
            print(qu,len(qu), "a=",a,"b=",b,"nx=", nx, "ny=", ny)
            for i in range(n):
                print(tomato[i])
         

for i in range(n):
    print(tomato[i])   
"""
isUnripe = False
result = -2
for row in tomato:
    for i in row:
        if i == 0:
            isUnripe = True
        result = max(i, result)

if isUnripe:  # 모두 익지 못하면
    print(-1)
elif result == 1:  # 이미 모두 익어있다면
    print(0)
else:  # 모두 익을 때까지 최소 날짜
    print(result-1)



