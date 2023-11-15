from collections import deque
n, m, k = map(int, input().split())
matrix = [[0 for column in range(m)] for row in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1


def bfs(x, y):
    qu = deque()
    qu.append((x, y))  # 큐 삽입
    matrix[x][y] = 0  # 방문처리
    cnt = 1  # 증가
    #print(qu, matrix, cnt)
    while qu:
        x, y = qu.popleft()  # 큐 빼오기
        for i in range(4):  # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            """
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if matrix[nx][ny] == 0:
                continue
            if matrix[nx][ny] == 1:
            """
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:  # 방문하지 않고 요소
                qu.append((nx, ny))  # 큐 삽입
                matrix[nx][ny] = 0  # 방문처리
                cnt += 1  # 증가
                # print(qu, "nx=",nx,"ny=",ny, matrix, cnt)
    return cnt


result = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            result = max(result, bfs(i, j))

print(result)


"""
from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
max_ = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    qu = deque()
    qu.append((x, y))
    while qu:
        x, y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                qu.append((nx, ny))

    return max(graph)


print(max(dfs(0, 0)))
"""




