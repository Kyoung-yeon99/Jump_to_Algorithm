# https://school.programmers.co.kr/learn/courses/30/lessons/154540

# 각 섬에서 최대 며칠씩 머무를 수 있는지
from collections import deque

def solution(maps):
    answer = []
    R, C = len(maps), len(maps[0])
    visited = [[False for _ in range(C)] for _ in range(R)]
    dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
    
    for i in range(R):
        for j in range(C):
            if not visited[i][j] and maps[i][j] != 'X': # 아직 방문하지 않은 섬일 경우
                visited[i][j] = True
                q = deque([(i, j)])
                days = int(maps[i][j])
                while q: # bfs
                    r, c = q.popleft()
                    for k in range(4): # 상하좌우
                        nr, nc = r + dr[k], c + dc[k]
                        if 0 <= nr < R and 0 <= nc < C: # 지도 범위 내
                            if not visited[nr][nc] and maps[nr][nc] != 'X': # 아직 방문지 않은 땅
                                visited[nr][nc] = True
                                q.append((nr, nc))
                                days += int(maps[nr][nc])
                answer.append(days) # 식량의 합 저장

    if answer: # 머물 수 있는 섬이 있을 경우
        answer.sort() # 오름차순 정렬
        return answer
    else: # 섬이 없는 경우
        return [-1]