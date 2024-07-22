# https://school.programmers.co.kr/learn/courses/30/lessons/250136
# 시간 초과
from collections import deque

def solution(land):
    n = len(land) # 가로 길이
    m = len(land[0]) # 세로 길이
    
    group = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    info = [[[0, 0] for _ in range(m)] for _ in range(n)]
    max_oil = 0
    dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
    
    for sc in range(m):
        for sr in range(n):
            if land[sr][sc] == 1 and not visited[sr][sc]:
                group.append([])
                visited[sr][sc] = True
                q = deque([(sr, sc)])
                while q:
                    r, c = q.popleft()
                    group[-1].append((r, c))
                    for i in range(4):
                        nr, nc = r + dr[i], c + dc[i]
                        if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1 and not visited[nr][nc]:
                            q.append((nr, nc))
                            visited[nr][nc] = True
            
    for num in range(len(group)):
        for pos in group[num]:
            oil = len(group[num])
            info[pos[0]][pos[1]] = [num, oil] 
            
    
    for c in range(m):
        drilled = {num: False for num in range(len(group))}
        total_oil = 0
        for r in range(n):
            num, oil = info[r][c]
            if oil > 0 and not drilled[num]:
                drilled[num] = True
                total_oil += oil
        max_oil = max(max_oil, total_oil)
    
    return max_oil