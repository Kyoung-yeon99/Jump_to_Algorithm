from collections import deque

m, n = map(int, input().split()) # 순서 주의
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

visited = [[-1] * m for _ in range(n)]  # 벽을 깬 횟수 저장

dxs = (1, 0, -1, 0)
dys = (0, 1, 0, -1)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs():
    q = deque()
    q.append([0, 0])  # 초기값 0,0 대입
    visited[0][0] = 0  # 벽을 깬 횟수 초기화

    while q:
        x, y = q.popleft()

        if x == n - 1 and y == m - 1:  # 도착
            return visited[x][y]

        for i in range(4):
            nx, ny = x + dxs[i], y + dys[i]
            if in_range(nx, ny) and visited[nx][ny] == -1:

                if graph[nx][ny] == 0:  # 방(가중치 0)
                    visited[nx][ny] = visited[x][y]
                    q.appendleft([nx, ny])
                else:  # 벽(가중치 1)
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])

    return -1  # 경로 없을 경우


print(bfs())
