from collections import deque
import sys

size = 2 # 아기 상어의 처음 크기
max_time = 0 # 최대 시간
sr, sc = None, None
found = False
n = int(input()) # 공간의 크기
a = [[] for _ in range(n)] # 공간에 대한 정보
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    if not found and 9 in row: # 아직 9의 위치를 찾지 못해고 row에 9가 존재할 경우
        found = True
        sr, sc= i, row.index(9)
    a[i] = row
visited = [[False for _ in range(n)] for _ in range(n)]
# 0: 빈 칸
# 1~6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치

# 몇 초 동안 계속해서 size보다 작은 수가 있는 칸으로 이동할 수 있는가
def getSize(count):
    i = 2
    if count < 4:
        return 2
    while count > i:
        count -= i
        i += 1
    return 2 + i

def bfs():
    global max_time
    q = deque()
    visited[sr][sc] = True
    time = 0
    q.append((sr, sc, visited, size, time))
    while q:
        r, c, v, s, t = q.popleft()
        print(r, c, v, s, t)
        for nr, nc in ((r+1, c),(r-1, c),(r, c+1),(r, c-1)):
            if 0 <= nr < n and 0 <= nc < n:
                if a[nr][nc] < s and not v[nr][nc]:
                    nv = v.copy()
                    nv[nr][nc] = True

                    q.append((nr, nc, nv, s+1, t+1))
        if time > max_time:
            max_time = time

bfs()
print(max_time)
