# https://velog.io/@sem/Baekjoon-2206-%EB%B2%BD-%EB%B6%80%EC%88%98%EA%B3%A0-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0-BFS-Python

from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # 방문 처리 리스트 [[벽 부순 적 O?, 벽 부순 적 X?] * M] * N개
visited[0][0][1] = 1


def bfs():
    queue = deque([[0, 0, 1]])  # 초기 출발 좌표 (0, 0) & 처음에는 벽 부순 적 없으니까 1

    dx = [-1, 1, 0, 0]  # 좌우
    dy = [0, 0, -1, 1]  # 상하

    while queue:
        y, x, w = queue.popleft()
        if y == N - 1 and x == M - 1:  # 도착
            return visited[y][x][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0 and visited[ny][nx][w] == 0:
                    visited[ny][nx][w] = visited[y][x][w] + 1  # 경로 길이
                    queue.append([ny, nx, w])

                if graph[ny][nx] == 1 and w == 1:  # 벽을 만났을 때 벽 부술 수 있는 횟수가 남아 있으면
                    visited[ny][nx][0] = visited[y][x][1] + 1  # 벽 부수고, 벽 부순적 있는 인덱스 값(0)으로 이전 위치 값 + 1 경로길이 할당
                    queue.append([ny, nx, 0])

    return -1


print(bfs())
