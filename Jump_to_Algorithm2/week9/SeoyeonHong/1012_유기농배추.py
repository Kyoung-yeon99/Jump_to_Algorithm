import sys
from collections import deque

input = sys.stdin.readline
T = int(input()) # 테스트 케이스 개수
for _ in range(T):
    M, N, K = map(int, input().split()) # 배추밭의 가로, 세로 길이, 배추 개수
    field = [] # 배추의 위치 정보
    checked = [[False for _ in range(M)] for _ in range(N)] # 배추 확인 여부
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    count = 0

    for i in range(K):
        X, Y = map(int, input().split())
        field.append((Y, X))
    
    # bfs
    q = deque()
    while field:
        if not q:
            q.append(field[0])
            count += 1
        else:
            r, c  = q.popleft()
            field.remove((r, c))
            checked[r][c] = True
            for i in range(4): # 상하좌우에 대해서
                nr, nc = r + dr[i], c + dc[i]
                if (nr, nc) in field and not checked[nr][nc]: # 근접한 곳에 아직 확인하지 않은 배추가 있을 경우
                    q.append((nr, nc))
                    checked[nr][nc] = True
    print(count)