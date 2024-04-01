# 최대 벽 1개를 부수고 이동할 때의 최단 경로
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split()) # 행, 열의 수
matrix = [] # 맵
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)] # 방문 여부 visited[행][열][벽을 부순 횟수]

for _ in range(N):
    matrix.append(input())

def bfs():
    q = deque([[0, 0, False]])
    visited[0][0][0] = 1 # 방문 여부 확인
    while q: # bfs
        x, y, wall = q.popleft()
        if x == N-1 and y == M-1: # 도착했을 경우
            return visited[x][y][wall] # 최단경로 출력
        for i in range(4): # 상하좌우에 대해
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][wall] == 0: # 아직 방문하지 않은 칸일 경우
                if matrix[nx][ny] == '0': # 벽이 아닐 경우
                    q.append([nx, ny, wall])
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                elif matrix[nx][ny] == '1' and wall == 0: # 벽이 존재하고 아직 벽을 부수지 않았다면
                    q.append([nx, ny, True])
                    visited[nx][ny][1] = visited[x][y][0] + 1
    return -1

print(bfs())