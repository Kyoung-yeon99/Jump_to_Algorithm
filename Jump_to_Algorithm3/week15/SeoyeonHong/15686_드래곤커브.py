# 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수를 구하는 프로그램
import sys

input = sys.stdin.readline
N = int(input())

dragon_curve = []
grid = [[False for _ in range(101)] for _ in range(101)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
answer = 0

for _ in range(N):
    dragon_curve.append(list(map(int, input().split())))

curve_directions = [] # 시작 방향에 따라 선이 이어지는 방향
curve_direction = [(1, 0)]
for _ in range(10):
    new_curve = []
    for x, y in curve_direction:
        new_curve.append((y, -x))
    new_curve.reverse()
    curve_direction.extend(new_curve)

curve_directions = [curve_direction]
for _ in range(10):
    new_curve_direction = []
    for x, y in curve_directions[-1]:
        new_curve_direction.append((y, -x))
    curve_directions.append(new_curve_direction)

for x, y, d, g in dragon_curve: # 각 드래곤 커브에 대해
    nx, ny = x, y
    cd = curve_directions[d]
    grid[x][y] = True
    for i in range(2 ** g): # 드래곤 커브에 속하는 꼭짓점 체크
        nx, ny = nx + cd[i][0], ny + cd[i][1]
        grid[nx][ny] = True

for ux in range(100):
    for uy in range(100):
        if grid[ux][uy] and grid[ux+1][uy] and grid[ux][uy+1] and grid[ux+1][uy+1]: # 네 꼭짓점이 모두 드래곤 커브의 일부라면
            answer += 1

print(answer)