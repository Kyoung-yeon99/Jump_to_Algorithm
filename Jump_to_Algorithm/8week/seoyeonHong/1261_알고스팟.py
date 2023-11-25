# 상하좌우로 이동 가능하나 벽(1)은 부수어야 지나갈 수 있음
# N, M으로 이동하기 위해 최소 몇 개의 벽을 부수어야 하는지 구하기
import heapq
import sys

m, n = map(int, sys.stdin.readline().split()) # 가로, 세로 크기
maze = [] # 미로의 상태
for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))
max = n*m
min = max
visited = [[max for _ in range(m)] for _ in range(n)]

def dijkstra():
    global min
    q = [] # 우선순위 큐
    heapq.heappush(q, (0, 0, 0))
    visited[0][0] = 0
    while q:
        cnt, r, c = heapq.heappop(q)
        if r == n-1 and c == m-1:
            if min > cnt:
                min = cnt
            continue
        for nr, nc in [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]:
            if 0 <= nr < n and 0 <= nc < m:
                ncnt = cnt + maze[nr][nc]
                if ncnt < min and visited[nr][nc] > ncnt:
                    visited[nr][nc] = ncnt
                    heapq.heappush(q, (ncnt, nr, nc)) # 벽을 부순 횟수를 기준으로 정렬

dijkstra()
print(min)

# bfs - 시간초과
# q = deque()
# q.append((0, 0, 0))
# while q:
#     r, c, cnt = q.popleft()
#     if r == n-1 and c == m-1:
#         if cnt < min:
#             min = cnt
#     for nr, nc in [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]:
#         if 0 <= nr < n and 0 <= nc < m: 
#             ncnt = cnt + int(maze[nr][nc])
#             if ncnt < min and visited[nr][nc] > ncnt:
#                 visited[nr][nc] = ncnt
#                 q.append((nr, nc, ncnt))
