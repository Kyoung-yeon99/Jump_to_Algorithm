import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000
table = [list(map(int, input().split())) for _ in range(n)]  # 원래 표
s = 0
t = [[0]*(n+1) for _ in range(n+1)]  # 누적합 저장할 표
for i in range(1, n+1):
    for j in range(1, n+1):
        t[i][j] = table[i - 1][j - 1] + t[i - 1][j] + t[i][j - 1] - t[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == x2 and y1 == y2:  # 같은 위치이면
        s = table[x1-1][y1-1]
    else:
        s = t[x2][y2] - t[x1-1][y2] - t[x2][y1-1] + t[x1-1][y1-1]

    print(s)




"""
# 시간초과 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    s = 0
    for i in range(x1-1, x2):
        s += sum(table[i][y1-1:y2])
    print(s)
"""
