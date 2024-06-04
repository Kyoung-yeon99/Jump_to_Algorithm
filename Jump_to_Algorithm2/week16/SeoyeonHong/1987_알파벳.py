# 같은 알파벳이 적힌 칸을 두 번 지날 수 없을 때 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램
# 오답
from collections import deque

R, C = map(int, input().split())
board = []
count = 0
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for _ in range(R):
    board.append(input())

q = deque([[0, 0, board[0][0]]])
while q:
    r, c, s = q.popleft()
    count = max(count, len(s))
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in s:
            q.append([nr, nc, s+board[nr][nc]])
    
print(count)