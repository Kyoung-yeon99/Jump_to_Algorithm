# 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값
import sys

input = sys.stdin.readline
N, M = map(int, input().split()) # 세로, 가로 크기
p = [] # 종이에 쓰인 숫자 배열
for _ in range(N):
    p.append(list(map(int, input().split())))
max_sum = 0
h = [[0 for _ in range(M)] for _ in range(N)]
v = [[0 for _ in range(M)] for _ in range(N)]

# 가로 2칸 합
for r in range(N):
    for c in range(M-1):
        h[r][c] = p[r][c] + p[r][c+1]

# 세로 2칸 합
for r in range(N-1):
    for c in range(M):
        v[r][c] = p[r][c] + p[r+1][c]

# 4*1, 1번 모양
for r in range(N-3):
    for c in range(M):
        max_sum = max(max_sum, v[r][c] + v[r+2][c])
        
# 1*4, 1번 모양
for r in range(N):
    for c in range(M-3):
        max_sum = max(max_sum, h[r][c] + h[r][c+2])

# 2*2, 2번 모양
for r in range(N-1):
    for c in range(M-1):
        max_sum = max(max_sum, h[r][c] + h[r+1][c])

# 3*2(세로 직사각형)
for r in range(N-2):
    for c in range(M-1):
        # 3*2의 합
        square = h[r][c] + h[r+1][c] + h[r+2][c] 

        # 3번 모양
        blank = min([v[r][c], v[r+1][c], v[r][c+1], v[r+1][c+1]])
        max_sum = max(max_sum, square - blank)
        
        # 4번 모양
        blank = min([p[r][c] + p[r+2][c+1], p[r][c+1] + p[r+2][c]])
        max_sum = max(max_sum, square - blank)
        
        # 5번 모양
        blank = min([p[r][c] + p[r+2][c], p[r][c+1] + p[r+2][c+1]])
        max_sum = max(max_sum, square - blank)
        
# 2*3(가로 직사각형)
for r in range(N-1):
    for c in range(M-2):
        # 2*3의 합
        square = v[r][c] + v[r][c+1] + v[r][c+2] 

        # 3번 모양
        blank = min([h[r][c], h[r+1][c], h[r][c+1], h[r+1][c+1]])
        max_sum = max(max_sum, square - blank)
        
        # 4번 모양
        blank = min([p[r][c] + p[r+1][c+2], p[r+1][c] + p[r][c+2]])
        max_sum = max(max_sum, square - blank)
        
        # 5번 모양
        blank = min([p[r][c] + p[r][c+2], p[r+1][c] + p[r+1][c+2]])
        max_sum = max(max_sum, square - blank)

print(max_sum)