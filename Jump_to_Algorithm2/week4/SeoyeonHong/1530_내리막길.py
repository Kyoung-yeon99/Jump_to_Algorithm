# dfs + dp
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
M, N = map(int, input().split()) # 지도의 세로, 가로 크기
m = [list(map(int, input().split())) for _ in range(M)] # 지도
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
dp = [[-1 for _ in range(N)] for _ in range(M)]

def searchWay(r, c):
    if r == 0 and c == 0: # 목표 지점에 도착했을 경우
         return 1
    if dp[r][c] == -1:
        dp[r][c] = 0
        for i in range(4): # 갈 수 있는 칸 탐색
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < M and 0 <= nc < N: # 지도 범위 안일 경우
                if m[r][c] < m[nr][nc]: # 높이가 더 낮으면
                    dp[r][c] += searchWay(nr, nc)
    return dp[r][c]
        
print(searchWay(M-1, N-1))


# 시간초과 - dfs
# import sys
# from collections import deque
# input = sys.stdin.readline
# M, N = map(int, input().split()) # 지도의 세로, 가로 크기
# m = [] # 지도
# w = 0 # 이동 가능한 경로의 수
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]

# for _ in range(M):
#     m.append(list(map(int, input().split())))

# def searchWay():
#     global w
#     q = deque()
#     q.append([0, 0])
#     while q:
#         r, c = q.pop()
#         if r == M-1 and c == N-1: # 목표 지점에 도착했을 경우
#             w += 1
#         else:
#             for i in range(4): # 갈 수 있는 칸 탐색
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if 0 <= nr < M and 0 <= nc < N: # 지도 범위 안일 경우
#                     if m[nr][nc] < m[r][c]: # 높이가 더 낮으면
#                         q.append([nr, nc])

# searchWay()
# print(w)


# 시간초과 - 백트래킹
# import sys
# input = sys.stdin.readline
# M, N = map(int, input().split()) # 지도의 세로, 가로 크기
# m = [] # 지도
# w = 0 # 이동 가능한 경로의 수
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]

# for _ in range(M):
#     m.append(list(map(int, input().split())))

# def searchWay(r, c, h):
#     global w
#     if r == M-1 and c == N-1: # 목표 지점에 도착했을 경우
#         w += 1
#     else:
#         for i in range(4): # 갈 수 있는 칸 탐색
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < M and 0 <= nc < N: # 지도 범위 안일 경우
#                 if m[nr][nc] < h[-1]: # 높이가 더 낮으면
#                     h.append(m[nr][nc])
#                     searchWay(nr, nc, h) # 이동
#                     h.pop()

# searchWay(0, 0, [m[0][0]])

# print(w)