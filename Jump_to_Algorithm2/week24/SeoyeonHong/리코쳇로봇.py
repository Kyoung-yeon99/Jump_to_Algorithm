# https://school.programmers.co.kr/learn/courses/30/lessons/169199

# 목표 위치까지의 최소 이동 횟수
from collections import deque

def solution(board):
    row, column = len(board), len(board[0]) # 보드의 행, 열 크기
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0] # 4방향
    q = deque([])
    visited = [[False for _ in range(column)] for _ in range(row)] # 방문 여부
    
    for i in range(row):
        if 'R' in board[i]:
            j = board[i].index('R')
            q.append((i, j, 0)) # 시작 위치 추가
            visited[i][j] = True
            break
    
    while q:
        r, c, d = q.popleft()
        
        for i in range(4): # 4방향에 대해서
            nr, nc = r, c
            
            while True: # 장애물이나 맨 끝에 부딪힐 때까지 이동
                nr += dr[i]
                nc += dc[i]
                if 0 <= nr < row and 0 <= nc < column and not board[nr][nc] == 'D':
                    continue
                else:
                    nr -= dr[i]
                    nc -= dc[i]
                    break
                
            if not visited[nr][nc]:
                visited[nr][nc] = True
                if board[nr][nc] == 'G': # 목표 위치에 도달했을 경우
                    return d+1 # 움직인 횟수 반환
                q.append((nr, nc, d+1))
    
    return -1 # 도착할 수 없을 경우