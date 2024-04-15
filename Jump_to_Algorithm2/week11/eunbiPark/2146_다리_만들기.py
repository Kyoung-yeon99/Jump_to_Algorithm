# 0: 바다, 1: 육지
from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
print('<<init - board>>')
for b in board:
    print(*b)
print()

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
                loc[num].append((nx, ny))

# 2. 최단 거리 판단 (모두 넣자)

loc = {}

# main
# 1. 섬 구분하기, 위치 등록
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

# 최단 거리 찾기
def bfs_shortest():
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            # 범위 내 방문하지 않았고, 물이라면
            if in_range(nx, ny) and not visited_shortest[nx][ny]:
                if visited[nx][ny] == 0:
                    print(nx, ny)
                    visited_shortest[nx][ny] = visited_shortest[x][y] -1 #
                    # cnt += 1
                    q.append((nx, ny))
                # 다른 섬 만났음
                elif visited[nx][ny] != i:
                    print(f'탈출: {nx, ny, x, y}')
                    return visited_shortest[x][y] - 1

print('vistied')
for v in visited:
    print(*v)
print()
print(f'loc:', loc)
# 2. 각 섬의 모든 부분에서 최단 거리 구하기
# mn = [] # 최솟값 저장
mn = float('inf')
for i in range(1, num): # i 번째 섬부터 체크
    q = deque()
    visited_shortest = [[0 for _ in range(n)] for _ in range(n)]

    # 초깃값 삽입, 방문 처리
    loc[i].sort(key = lambda x: (-x[0], x[1]))
    for x, y in loc[i]:
        q.append((x, y))
        visited_shortest[x][y] = i # 섬 표시

    mn = min(-bfs_shortest(), mn)

    print(mn)

    print('<<shortest visited>>')
    for s in visited_shortest:
        print(*s)
    print()

print(mn)
