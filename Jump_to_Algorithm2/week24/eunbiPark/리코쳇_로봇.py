from collections import deque
def solution(board):
    n = len(board)
    m = len(board[0])
    
    dxs, dys = [0, 0, 1, -1], [-1, 1, 0, 0]
    
    # 로봇 초기 위치 등록
    for i in range(n):    
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
    
    # bfs 사전 준비
    q = deque()
    q.append((rx, ry))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[rx][ry] = 1
    
    # 범위 체크 함수
    def in_range(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        return True
    
    # 이동 함수 - 한 번에 미끌어지듯 이동
    def move(x, y, dx, dy):
        nx, ny = x + dx, y + dy
        while in_range(nx, ny) and board[nx][ny] != 'D':
            nx += dx
            ny += dy
            
        return nx - dx, ny - dy
    
    def bfs():
        while q:
            x, y = q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = move(x, y, dx, dy) # nx, ny = x + dx, y + dy를 변경
                if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] != 'D':
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    
                    # 종료 조건
                    if board[nx][ny] == 'G':
                        return visited[x][y]
        
        # G 만나지 못하면 -1 리턴
        return -1
    
    ans = bfs()
    
    return ans
