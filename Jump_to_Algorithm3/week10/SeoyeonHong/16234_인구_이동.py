# 인구 이동이 며칠 동안 발생하는지 구하는 프로그램
from collections import deque

N, L, R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

visited = [[False for _ in range(N)] for _ in range(N)]
dr, dc = [1, 0 , -1, 0], [0, 1, 0, -1]

def check_union(sr, sc):
    global A
    global visited
    union = [(sr, sc)]
    total_population = A[sr][sc]
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    while q: # bfs 
        r, c = q.popleft()
        for i in range(4): # 인접한 국가들에 대해
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(A[r][c] - A[nr][nc]) <= R: # 인구 이동 조건을 만족한다면
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    union.append((nr, nc))
                    total_population += A[nr][nc]

    average = total_population // len(union) # 연합을 이루는 국가들의 인구수의 평균
    changed = False
    for r, c in union:
        if A[r][c] != average:
            changed = True
            A[r][c] = average
    
    return changed # 인구이동 발생 여부 반환

day = 0 # 인구이동이 발생한 기간
while True:
    changed = False # 인구이동 발생 여부 초기화
    visited = [[False for _ in range(N)] for _ in range(N)] # 방문 여부 초기화

    for r in range(N): # 각 나라에 대해
        for c in range(N):
            if not visited[r][c]: # 아직 방문하지 않았다면
                if check_union(r, c): # 연합을 이루는 국가 확인 및 인구 이동
                    changed = True 
    if not changed: # 인구 이동이 일어나지 않았다면
        print(day) # 일수 출력 및 종료
        break
    else: # 인구 이동이 일어났다면
        day += 1 # 일수 +1 
