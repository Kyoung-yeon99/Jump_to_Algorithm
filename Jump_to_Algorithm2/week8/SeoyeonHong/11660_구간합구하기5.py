import sys

input = sys.stdin.readline
N, M = map(int, input().split()) # 표의 크기, 합을 구해야 하는 횟수
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

part_sum = [[0 for _ in range(N)] for _ in range(N)] # part_sum[i][j] == (0,0)과 (i,j)를 꼭짓점으로 가지는 사각형의 합
for x in range(N):
    column_sum = 0
    for y in range(N):
        sum = 0
        row_sum = 0
        if x > 0:
            row_sum = part_sum[x-1][y]
        if y > 0:
            column_sum += arr[x][y-1]
        part_sum[x][y] = row_sum + column_sum + arr[x][y]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    sum = part_sum[x2][y2]
    if x1 != 0: # 위쪽 사각형 합 빼기
        sum -= part_sum[x1-1][y2]
    if y1 != 0: # 왼쪽 사각형 합 빼기
        sum -= part_sum[x2][y1-1]
    if x1 != 0 and y1 != 0: # 중복되는 빼기 방지
        sum += part_sum[x1-1][y1-1]
    print(sum)