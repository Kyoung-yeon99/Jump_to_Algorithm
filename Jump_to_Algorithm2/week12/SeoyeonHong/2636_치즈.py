# 공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수
import sys
from collections import deque

input = sys.stdin.readline
R, C = map(int, input().split())
arr = []
time = 0
cheese = 0
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
outline = deque([])
last_cheeze = 0

for _ in range(R):
    row = list(map(int, input().split()))
    cheese += row.count(1)
    arr.append(row)

def check_outline():
    global cheese
    q = deque([(0, 0)])
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[0][0] = True

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc]:
                    if arr[nr][nc] == 1:
                        arr[nr][nc] = 0
                        cheese -= 1
                    else: 
                        q.append((nr, nc))
                    visited[nr][nc] = True
                    
while cheese > 0:
    time += 1
    last_cheeze = cheese
    check_outline()

print(time) # 치즈가 모두 녹아 없어지즌 데 걸리는 시간
print(last_cheeze) # 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수
