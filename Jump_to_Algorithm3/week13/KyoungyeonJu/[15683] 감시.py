import sys
from itertools import product
from copy import deepcopy
input = sys.stdin.readline
# 사각 지대의 최소 크기
n, m = map(int, input().split())  # 1 <= N, M <= 8
matrix = [list(map(int, input().split())) for _ in range(n)]


def up(r, c):
    for i in range(r, -1, -1):
        #print(i, c)
        if map[i][c] == 6:
            break
        elif map[i][c] == 0:
            map[i][c] = 7


def right(r, c):
    for i in range(c, m):
        #print(r, i)
        if map[r][i] == 6:
            break
        elif map[r][i] == 0:
            map[r][i] = 7


def down(r, c):
    for i in range(r, n):
        #print(i, c)
        if map[i][c] == 6:
            break
        elif map[i][c] == 0:
            map[i][c] = 7


def left(r, c):
    for i in range(c, -1, -1):
        #print(r, i)
        if map[r][i] == 6:
            break
        elif map[r][i] == 0:
            map[r][i] = 7


def cctv_1(r, c, case):
    #print("cctv_1", r, c, case)
    if case == 0: up(r, c)
    elif case == 1: right(r, c)
    elif case == 2: down(r, c)
    elif case == 3: left(r, c)


def cctv_2(r, c, case):
    #print("cctv_2", r, c, case)
    if case == 0:
        left(r, c)
        right(r, c)
    elif case == 1:
        up(r, c)
        down(r, c)


def cctv_3(r, c, case):
    #print("cctv_3", r, c, case)
    if case == 0:
        up(r, c)
        right(r, c)
    elif case == 1:
        right(r, c)
        down(r, c)
    elif case == 2:
        down(r, c)
        left(r, c)
    elif case == 3:
        left(r, c)
        up(r, c)


def cctv_4(r, c, case):
    #print("cctv_4", r, c, case)
    if case == 0:
        left(r, c)
        up(r, c)
        right(r, c)
    elif case == 1:
        up(r, c)
        right(r, c)
        down(r, c)
    elif case == 2:
        right(r, c)
        down(r, c)
        left(r, c)
    elif case == 3:
        down(r, c)
        left(r, c)
        up(r, c)


def cctv_5(r, c):
    #print("cctv_5", r, c)
    up(r, c)
    right(r, c)
    down(r, c)
    left(r, c)



# 방향이 필요한 CCTV 1,2,3,4
# 1은 동/서/남/북, 2는 동서/남북, 3은 북동/동남/남서/서북, 4는 각 동/서/남/북 빼고
# 각 CCTV 위치, 개수, case
cctv = [[] for _ in range(6)]
cctv_product = []
answer = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            answer += 1
        elif matrix[i][j] < 6:
            cctv[matrix[i][j]].append([i, j])

for i in range(1, 5):
    if i == 2:
        for _ in range(len(cctv[i])):
            cctv_product.append([0, 1])
    else:
        for _ in range(len(cctv[i])):
            cctv_product.append([0, 1, 2, 3])
#print("cctv", cctv)
#print(cctv_product)
for p in product(*cctv_product):
    #print("p", p)
    map = deepcopy(matrix)

    # 중복순열, 함수 호출
    idx = 0
    for i in range(1, 5):
        for r, c in cctv[i]:
            if i == 1:
                cctv_1(r, c, p[idx])
            elif i == 2:
                cctv_2(r, c, p[idx])
            elif i == 3:
                cctv_3(r, c, p[idx])
            elif i == 4:
                cctv_4(r, c, p[idx])
            idx += 1

    for r, c in cctv[5]:
        cctv_5(r, c)

    cnt_0 = sum(row.count(0) for row in map)
    answer = min(answer, cnt_0)

print(answer)