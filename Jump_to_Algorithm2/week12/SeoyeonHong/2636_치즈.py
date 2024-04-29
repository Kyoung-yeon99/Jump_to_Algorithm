# 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수
import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
arr = []
time = 0 # 시간
cheese = 0 # 치즈조각이 놓인 칸의 개수
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
last_cheese = 0

for _ in range(R):
    row = list(map(int, input().split()))
    cheese += row.count(1) # 초기 치즈 개수 계산
    arr.append(row)

def check_outline(): # 공기에 노출된 외곽부분 확인
    global cheese
    q = deque([(0, 0)]) # 치즈가 없는 (0, 0) 부터 탐색 시작
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[0][0] = True

    while q: # 너비우선 탐색
        r, c = q.popleft()
        for i in range(4): # 인접한 네 방향에 대해
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C: # 판을 벗어나지 않는 경우
                if not visited[nr][nc]: # 아직 방문하지 않은 경우
                    if arr[nr][nc] == 1: # 치즈가 있는 칸이면
                        arr[nr][nc] = 0
                        cheese -= 1
                    else: # 치즈가 없는 칸이면
                        q.append((nr, nc))
                    visited[nr][nc] = True
                    
while cheese > 0: # 치즈가 다 녹을 때까지
    time += 1
    last_cheese = cheese # 가장 최근의 치즈조각이 놓인 칸의 개수
    check_outline() # 녹은 치즈 확인

print(time) # 치즈가 모두 녹아 없어지즌 데 걸리는 시간
print(last_cheese) # 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수
