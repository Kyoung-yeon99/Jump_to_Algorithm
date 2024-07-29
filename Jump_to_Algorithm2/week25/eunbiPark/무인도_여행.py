# x: 바다, 1~9: 무인도, 식량
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    ans = [] 
    
    def in_range(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False 
        return True
    
    def bfs():
        days = 0
        while q:
            x, y = q.popleft()
            days += int(maps[x][y])
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                
        return days

    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = 1
                ans.append(bfs())
        
    return sorted(ans) if len(ans) else [-1]
