# 잃을 수 밖에 없는 최소 금액
import sys
import heapq

input = sys.stdin.readline
N, T = 0, 0 # 동굴의 크기, 테스트 케이스 번호
rupee, visited, loss = [], [], [] # 루피의 크기, 방문 여부, 최소 피해 금액
ad = [] # 인접 리스트
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dijkstra():
    loss[0][0] = rupee[0][0]
    q = [] # (최소 피해 금액, [행, 열])
    heapq.heappush(q, (loss[0][0], [0, 0]))

    while q:
        l, p = heapq.heappop(q) # 탐색할 칸과 루피의 크기
        if loss[p[0]][p[1]] < l:
            continue
        for r, c in ad[p[0]][p[1]]:
            if l + rupee[r][c] < loss[r][c]:
                loss[r][c] = l + rupee[r][c]
                heapq.heappush(q, (l + rupee[r][c], [r, c]) )  
    
    
while True:
    N = int(input())
    if N == 0: # 0이 입력되면 종료
        exit()
    T += 1 # t번째 테스트 케이스
    ad = [[[] for _ in range(N)] for _ in range(N)]
    rupee = [] # 각 칸에 존재하는 루피 정보
    visited = [[False for _ in range(N)] for _ in range(N)]
    loss = [[10 * N * N for _ in range(N)] for _ in range(N)]
    for _ in range(N):
        rupee.append(list(map(int, input().split())))

    # 인접 리스트 업데이트
    for r in range(N):
        for c in range(N):
            if r > 0:
                ad[r][c].append([r-1, c])
            if r < N-1:
                ad[r][c].append([r+1, c])
            if c > 0:
                ad[r][c].append([r, c-1])
            if c < N-1:
                ad[r][c].append([r, c+1])
    
    dijkstra()

    print(f'Problem {T}: {loss[N-1][N-1]}')


# 시간초과
# import sys
# from collections import deque
# import heapq

# input = sys.stdin.readline
# N, T = 0, 0 # 동굴의 크기, 테스트 케이스 번호
# rupee, visited, loss = [], [], [] # 루피의 크기, 방문 여부, 최소 피해 금액
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]

# def move(): # 출구까지 가는 길 탐색
#     global visited
#     q = deque()
#     q.append([0, 0]) # 출발 위치
#     loss[0][0] = rupee[0][0]
#     visited[0][0] = True

#     while q:
#         r, c = q.pop()
#         print(f'search {rupee[r][c]} ({r}, {c})')
#         if r != N-1 or c != N-1: # 출구가 아니라면
#             np = [] # 이동할 수 있는 다음 칸
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if 0 <= nr < N and 0 <= nc < N: # 동굴 내부일 경우
#                     heapq.heappush(np, [nr, nc]) # 이동할 칸 목록에 추가
            
#             while np:
#                 nr, nc = heapq.heappop(np)
#                 nl = loss[r][c] + rupee[nr][nc]
#                 if not visited[nr][nc]: # 처음 방문하는 칸일 경우
#                     visited[nr][nc] = True
#                     loss[nr][nc] = nl
#                     if nl < loss[N-1][N-1]:
#                         q.append([nr, nc])
#                 elif loss[nr][nc] >= nl and nl < loss[N-1][N-1]:
#                     loss[nr][nc] = nl   
#                     q.append([nr, nc])
#         for row in loss:
#             print(*row)
#         print('-----------------')
    
# while True:
#     N = int(input())
#     if N == 0: # 0이 입력되면 종료
#         exit()
#     T += 1 # t번째 테스트 케이스
#     rupee = [] # 각 칸에 존재하는 루피 정보
#     visited = [[False for _ in range(N)] for _ in range(N)]
#     loss = [[10 * N * N for _ in range(N)] for _ in range(N)]
#     for _ in range(N):
#         rupee.append(list(map(int, input().split())))
#     move()
#     print(f'Problem {T}: {loss[N-1][N-1]}')