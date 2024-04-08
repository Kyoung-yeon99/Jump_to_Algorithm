# 벽 3개를 세워서 얻을 수 있는 안전 영역 크기의 최댓값
import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline
# 0: 빈 칸, 1: 벽, 2: 바이러스
N, M = map(int, input().split()) # 세로 크기, 가로 크기
original_info = [] # 지도 원본
info = []
original_virus = [] # 초기 바이러스 위치
virus = []
original_vacant = []
visited = [[False for _ in range(M)] for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
max_safe_zone = 0 # 안전 영역 크기 최댓값

for r in range(N):
    original_info.append(list(map(int, input().split())))
    for c in range(M):
        if original_info[r][c] == 2: # 바이러스 위치 저장
            original_virus.append((r, c))
        elif original_info[r][c] == 0: # 빈 공간 저장
            original_vacant.append((r, c))

def check_virus():
    global info
    global virus
    new_virus = []
    for r, c in virus:
        for i in range(4):
            ar, ac = r + dr[i], c + dc[i]
            if 0 <= ar < N and 0 <= ac < M and info[ar][ac] == 0:
                new_virus.append((ar, ac))
                info[ar][ac] = 2
    virus = new_virus

def check_safe_zone(sr, sc):
    global visited
    global max_safe_zone

    safe_zone = 0
    visited[sr][sc] = True
    q = deque([(sr, sc)])

    while q:
        safe_zone += 1 # 안전 영역의 크기 + 1
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and info[nr][nc] == 0 and not visited[nr][nc]: # 아직 방문하지 않은 빈 공간일 경우
                visited[nr][nc] = True
                q.append((nr, nc))
    return safe_zone
                
for combination in combinations(original_vacant, 3): # 3개의 벽을 추가하는 모든 경우에 대해
    info = copy.deepcopy(original_info)
    virus = copy.deepcopy(original_virus)
    visited = [[False for _ in range(M)] for _ in range(N)]
    total_safe_zone = 0

    for r, c in combination: # 원본 지도의 복사본 info에 3개의 벽 추가
        info[r][c] = 1
    
    while virus != []: # 바이러스가 더 이상 퍼지지 않을 경우 빈 배열
        check_virus()

    for r in range(N): 
        for c in range(M):
            if info[r][c] == 0 and not visited[r][c]:
                visited[r][c] = True
                total_safe_zone += check_safe_zone(r, c) # 모든 안전 영역의 합 계산
    max_safe_zone = max(max_safe_zone, total_safe_zone) # 안전 영역 크기 최댓값 갱신

print(max_safe_zone)