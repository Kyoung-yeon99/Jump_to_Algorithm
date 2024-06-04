# 만날 수 있는 사람의 수 구하기
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
campus = []
pos = [0, 0] # 현재 위치
visited = [[False for _ in range(M)] for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
people = 0 # 만날 수 있는 사람의 수

for r in range(N):
    row = input()
    for c in range(M):
        if row[c] == 'I':
            pos = [r, c] # 현재 위치 저장
    campus.append(row)

# bfs
q = deque([pos])
visited[pos[0]][pos[1]] = True
while q:
    r, c = q.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]: # 아직 방문하지 않은 캠퍼스 내의 공간일 경우
            if campus[nr][nc] != 'X': # 벽이 아니라면
                if campus[nr][nc] == 'P': # 사람이 있다면
                    people += 1
                q.append([nr, nc])
                visited[nr][nc] = True

print('TT') if people == 0 else print(people)
                

