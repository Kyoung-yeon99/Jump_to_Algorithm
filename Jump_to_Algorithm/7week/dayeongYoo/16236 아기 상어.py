# 공간 크기
from collections import deque

n = int(input())
# 공간의 상태(0: 빈 칸, # 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기, 9: 아기 상어의 위치)
board = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우로 이동
dxs = (-1, 1, 0, 0)
dys = (0, 0, -1, 1)

# 아기상어 크기, 섭취한 물고기, 총 물고기 수
size, eat_cnt, fish_cnt = 2, 0, 0
# 물고기 위치 저장
fish_pos = []
# 아기상어 위치
sx, sy = 0, 0
# 시간
time = 0

# 1. 공간에서 아기상어, 물고기가 있는 칸 먼저 찾아야 함
for i in range(n):
    for j in range(n):
        if board[i][j] == 9: # 아기상어 위치
            sx, sy = i, j
        elif 0 < board[i][j] <= 6:  # 물고기가 있는 칸이라면
            fish_cnt += 1
            fish_pos.append((i, j))
# 아기상어 좌표
board[sx][sy] = 0


# bfs
def bfs(sx, sy):
    q = deque([(sx, sy, 0)]) # 큐 생성
    dists = []
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    min_dist = int(1e9)  # 최단거리는 무한으로 초기화
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] <= size:  # (nx,ny) 위치의 물고기가 아기상어보다 작거나 같다면
                    visited[nx][ny] = True  # 아기상어 이동
                    if 0 < board[nx][ny] < size:  # 크기가 작은 물고기라면 먹을 수 있다
                        min_dist = dist  # 자금까지 이동한 거리
                        dists.append((dist + 1, nx, ny))  # 이동한 거리 및 위치 저장
                    if dist + 1 <= min_dist:
                        q.append((nx, ny, dist + 1))  # 상어가 이동할 다음 좌표 및 최소거리 큐에 추가
    if dists:
        dists.sort()  # dists[0]으로 상어가 이동한 총 거리 쉽게 구하기 위해 정렬한다.
        return dists[0]
    else:
        return False


while fish_cnt:
    res = bfs(sx, sy)
    if not res: # 갈 수 없을 경우 종료
        break
    sx, sy = res[1], res[2] # x좌표 y 좌표

    time += res[0] # 이동한거리 == 이동시간(1초에 한칸씩 이동)

    eat_cnt += 1  # 먹은 물고기 수로 상어 크기 측정
    fish_cnt -= 1  # 한번 돌때 물고기는 한번만 섭취 가능

    if size == eat_cnt:  # 크기가 같고 같은 물고기 섭취시
        size += 1  # 상어 성장
        eat_cnt = 0  # 초기화
    board[sx][sy] = 0

print(time)
