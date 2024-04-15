# 두 대륙을 연결하는 가장 짧은 다리의 길이
import sys
from collections import deque

input = sys.stdin.readline
N = int(input()) # 섬의 크기
m = [] # 지도
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
inland = [[False for _ in range(N)] for _ in range(N)]
continent = [[0 for _ in range(N)] for _ in range(N)]
length = 0 # 다리의 길이

for _ in range(N):
    m.append(list(map(int, input().split())))

def check_continent(sr, sc, cont, m, visited): # 섬의 번호 표시

    visited[sr][sc] = True
    q = deque([(sr, sc)])

    while q: # bfs
        r, c = q.popleft()
        m[r][c] = cont

        for i in range(4): # 동서남북에 대해
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if m[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append([nr, nc])

def extend_continent(m):
    global length
    connected = False
    min_extend = 2 # 모든 섬이 확장했을 경우 다리 길이+2
    extended = [[False for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if m[r][c] > 0 and not extended[r][c] and not inland[r][c]:
                way = 0
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if m[nr][nc] == 0: # 바다와 접해 있을 경우
                            m[nr][nc] = m[r][c] # 섬 확장
                            extended[nr][nc] = True
                            for j in range(4): # 확장한 칸이 다른 섬과 맞닿는지 확인
                                ar, ac = nr + dr[j], nc + dc[j]
                                if 0 <= ar < N and 0 <= ac < N:
                                    if m[ar][ac] != 0 and m[ar][ac] != m[r][c]:
                                        if extended[ar][ac] == False: # 하나의 섬만 확장됐을 경우 다리 길이+1
                                            min_extend = 1
                                        connected = True
                            way += 1
                        elif m[nr][nc] != m[r][c]: # 확장한 칸이 다른 섬일 경우
                            connected = True
                if way == 0: # 확장할 수 없는 경우
                    inland[r][c] = True
    length += min_extend
    return connected

cont = 0 # 섬의 번호
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if m[i][j] == 1 and not visited[i][j]:
            cont += 1
            check_continent(i, j, cont, m, visited)

connected = False

while not connected:
    connected = extend_continent(m)

print(length)


    
