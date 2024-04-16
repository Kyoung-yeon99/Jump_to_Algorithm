# 0: 바다, 1: 육지
from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

# 1. 섬 구분
def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny] = num
                q.append((nx, ny))
                loc[num].append((nx, ny)) # 위치 등록

# 2. 최단 거리 판단 (모두 넣자)
def bfs_shortest():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                # 물이고, 방문하지 않았다면
                if visited[nx][ny] == 0 and visited_shortest[nx][ny] == -1:
                    # 거리 생신
                    visited_shortest[nx][ny] = visited_shortest[x][y] + 1
                    q.append((nx, ny))
                # 섬이고, 출발한 섬이 아니라면
                elif visited[nx][ny] and visited[nx][ny] != i:
                    # 거리 리턴
                    return visited_shortest[x][y]

# main
# 1. 섬 구분하기, 위치 등록
loc = {} # 각 섬의 위치 정보
q = deque()
visited = [[0 for _ in range(n)] for _ in range(n)]
num = 1
for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j]:
            loc[num] = [(i, j)] # dict 생성 - 섬의 위치 저장
            q.append((i, j))
            visited[i][j] = num
            bfs()
            num += 1

# 2. 각 섬의 모든 부분에서 최단 거리 구하기
mn = float('inf')
for i in range(1, num): # i 번째 섬부터 체크
    q = deque()
    visited_shortest = [[-1 for _ in range(n)] for _ in range(n)]

    # 초깃값 삽입, 방문 처리
    for x, y in loc[i]:
        q.append((x, y))
        visited_shortest[x][y] = 0 # 섬 표시

    mn = min(bfs_shortest(), mn)

print(mn)
