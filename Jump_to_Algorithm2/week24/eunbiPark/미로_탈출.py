from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    ans = 0
    dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i, j
    
    def in_range(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False 
        return True

    def bfs(goal):
        while q:
            x, y = q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and not visited[nx][ny] and maps[nx][ny] != 'X':
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

                    if not goal and maps[nx][ny] == 'L':
                        return nx, ny, visited[nx][ny] - 1
                    
                    if goal and maps[nx][ny] == 'E':
                        return nx, ny, visited[nx][ny] - 1
                    
        return -1, -1, -1
                
                
    # 1. 레버 돌리기
    q = deque()
    q.append((sx, sy))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[sx][sy] = 1
    lx, ly, ans = bfs(False)
    
    # 2. 출구 찾기 
    q = deque()
    q.append((lx, ly))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[lx][ly] = 1
    _, _, temp = bfs(True)
    
    return -1 if temp == -1 else ans + temp
    
