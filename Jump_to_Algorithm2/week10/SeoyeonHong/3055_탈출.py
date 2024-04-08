# 고슴도치가 비버의 굴로 이동하기 위해 필요한 최소 시간
import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split()) # 행, 열
info = [] # 지도
visited = [[False for _ in range(C)] for _ in range(R)] # 방문 여부
S, D = [], [] # 고슴도치와 비버굴의 위치
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
time = 0
flood = []

for r in range(R):
    info.append(list(input()))
    for c in range(C):
        i = info[r][c]
        if i == 'D':
            D = [r, c]# 비버 위치 저장
        elif i == 'S':
            info[r][c] = '.' # 침수 가능한 위치이므로 '.'로 변경
            S = [r, c] # 고슴도치 위치 저장
        elif i == '*':
            flood.append([r, c])

def check_flood():
    global info
    global flood
    new_flood = []
    for fr, fc in flood:
        for i in range(4):
            ar, ac = fr + dr[i], fc + dc[i]
            if 0 <= ar < R and 0 <= ac < C and info[ar][ac] == '.':
                new_flood.append((ar, ac))
                info[ar][ac] = '*'
    flood = new_flood   

def find_way():
    global time
    q = deque([[S[0], S[1], 0]])
    visited[S[0]][S[1]] = True
    while q:
        r, c, t = q.popleft()
        if time != t: # 시간이 지났을 경우
            check_flood() # 물이 차있는 지역 확인
            time = t
        if r == D[0] and c == D[1]:
            time = t
            return True
        for i in range(4): # 인접한 네 칸에 대해
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                if info[nr][nc] != '*' and info[nr][nc] != 'X': # 갈 수 있다면
                    visited[nr][nc] = True
                    q.append([nr, nc, t+1])   
    return False
        
# 길 찾기
check_flood()
if find_way(): # 탈출 했을 경우
    print(time) 
else:
    print("KAKTUS") # 실패 시


