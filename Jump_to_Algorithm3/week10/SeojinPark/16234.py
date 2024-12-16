import sys
from collections import deque
input = sys.stdin.readline

N, L, R= map(int, input().split())
nations=[]
for _ in range(N):
    nation = list(map(int, input().split()))
    nations.append(nation)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque()
    union = []
    queue.append((x, y))
    union.append((x, y))

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx <N and 0<= ny<N and visited[nx][ny] == 0:
                if L <= abs(nations[nx][ny]-nations[a][b]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union

result =0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                if len(country)>1:
                    flag = 1
                    people = sum(nations[x][y] for x, y in country)//len(country)
                    for x, y in country:
                        nations[x][y] = people
    if flag==0:
        print(result)
        break
    result += 1

