# https://school.programmers.co.kr/learn/courses/30/lessons/159993

# 미로를 탈출하는데 필요한 최소 시간
from collections import deque

def solution(maps):
    R, C = len(maps), len(maps[0]) # 행과 열의 크기
    v1 = [[False for _ in range(C)] for _ in range(R)] # 방문 여부 확인
    v2 = [[False for _ in range(C)] for _ in range(R)] # 방문 여부 확인
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0] # 4방향
    
    s = [] # 시작 위치
    found = False
    for i in range(R):
        if 'S' in maps[i]:
            s = [i, maps[i].index('S')]
            found = True
        if found:
            break
        

    cnt = 0 # 이동 시간
    found = False
    q = deque([[s[0], s[1], cnt]])
    
    while q:
        r, c, cnt= q.popleft()
        for i in range(4): # 4방향에 대해
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] != 'X' and not v1[nr][nc]: # 아직 가지 않은 곳이면
                if maps[nr][nc] == 'L': # 레버가 있다면
                    found = True
                    q = deque([[nr, nc, cnt+1]])
                    break
                v1[nr][nc] = True
                q.append([nr, nc, cnt+1])
        if found:
            break
    
    if not found:
        return -1
    else:
        found = False
        while q:
            r, c, cnt = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and maps[nr][nc] != 'X' and not v2[nr][nc]: # 아직 가지 않은 곳이면
                    if maps[nr][nc] == 'E': # 출구일 경우
                        found = True
                        cnt += 1
                        break
                    v2[nr][nc] = True
                    q.append([nr, nc, cnt+1])
            if found:
                break
        if not found:
            return -1
        else:
            return cnt