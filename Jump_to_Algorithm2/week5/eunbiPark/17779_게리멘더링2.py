n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
numbers = [[0 for _ in range(n)] for _ in range(n)]
ans = float('inf')


def draw():
    # 1 번 구역 경계 표시
    for delta in range(w + 1):
        # 상 -> 좌
        numbers[i + delta][j - delta] = 1
        # 우 -> 하
        numbers[i + h + delta][j + h - delta] = 1
    for delta in range(1, h):
        # 상 -> 우
        numbers[i + delta][j + delta] = 1
        # 좌 -> 하
        numbers[i + w + delta][j - w + delta] = 1

    # 직선 경계 표시 
    for x in range(i):
        numbers[x][j] = 2
    for y in range(j + h + 1, n):
        numbers[i + h][y] = 3
    for y in range(j - w):
        numbers[i + w][y] = 4
    for x in range(i + w + h + 1, n):
        numbers[x][j - w + h] = 5

    # 2번 채우기 
    for x in range(i + w):
        for y in range(j):
            if numbers[x][y] != 0:
                break
            numbers[x][y] = 2

    # 3번 채우기 
    for x in range(i + h):
        for y in range(n - 1, j, -1):
            if numbers[x][y] != 0:
                break
            numbers[x][y] = 3

            # 4번 채우기
    for x in range(i + w, n):
        for y in range(j - w + h):
            if numbers[x][y] != 0:
                break
            numbers[x][y] = 4

            # 5번 채우기
    for x in range(i + h + 1, n):
        for y in range(n - 1, j - w + h, -1):
            if numbers[x][y] != 0:
                break
            numbers[x][y] = 5


def in_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True


# 지역별 인구수 계산, 최대 - 최소
def calc():
    total = [0, 0, 0, 0, 0, 0]
    for i in range(n):
        for j in range(n):
            total[numbers[i][j]] += board[i][j]

    # 직사각형 내부 1번 처리 
    total[1] += total[0]
    total.pop(0)  # min 계산하기위해 제거

    return (max(total) - min(total))


# 1. 가로, 세로 설정
for w in range(1, 2 * n):
    for h in range(1, 2 * n):
        # 2. 시작 좌표 설정 (맨 위)
        for i in range(n):
            for j in range(n):
                # 3. 범위 확인 (상, 좌, 하, 우)
                if in_range(i, j) and in_range(i + w, j - w) and \
                        in_range(i + w + h, j - w + h) and in_range(i + h, j + h):
                    numbers = [[0 for _ in range(n)] for _ in range(n)]
                    # 4. 경계 표시 
                    draw()
                    # 5. 구역별 인구수 계산, 갱신
                    ans = min(ans, calc())

print(ans)

'''
# sol_2
import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

border = [
    [False for _ in range(n)]
    for _ in range(n)
]

total_sum = 0


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 가장 아래 지점을 제외한 3개의 꼭지점이 전부
# 격자 안에 들어오는 경우에만 해당 직사각형을 그릴 수 있습니다.
def possible_to_draw(x, y, k, l):
    return in_range(x - k, y + k) and in_range(x - k - l, y + k - l) \
       and in_range(x - l, y - l)


def draw_slanted_rect_border(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]

    # 먼저 border값을 전부 false로 초기화합니다.
    for i in range(n):
        for j in range(n):
            border[i][j] = False

    # 기울어진 직사각형의 경계를 쭉 따라가봅니다.
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy
            border[x][y] = True

# 구역 확인과 동시에 계산
def get_score(x, y, k, l):
    population = [0, 0, 0, 0, 0]

    # 경계를 표시합니다.
    draw_slanted_rect_border(x, y, k, l)

    # 좌측 상단 구역
    for i in range(x - l):
        for j in range(y + k - l + 1):
            if border[i][j]:
                break

            population[0] += grid[i][j]

    # 좌측 하단 구역
    for i in range(x - l, n):
        for j in range(y):
            if border[i][j]:
                break

            population[1] += grid[i][j]

    # 우측 상단 구역
    for i in range(x - k + 1):
        for j in range(n - 1, y + k - l, -1):
            if border[i][j]:
                break

            population[2] += grid[i][j]

    # 우측 하단 구역
    for i in range(x - k + 1, n):
        for j in range(n - 1, y - 1, -1):
            if border[i][j]:
                break

            population[3] += grid[i][j]

    population[4] = total_sum - sum(population[:4])
    return max(population) - min(population)


total_sum = sum([
    grid[i][j]
    for i in range(n)
    for j in range(n)
])

ans = INT_MAX

# (i, j)를 시작으로 1, 2, 3, 4 방향
# 순서대로 길이 [k, l, k, l] 만큼 이동하면 그려지는
# 기울어진 직사각형을 잡아보는
# 완전탐색을 진행해봅니다.
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                # 직사각형을 그릴 수 있는 경우에만
                # 답을 갱신합니다.
                if possible_to_draw(i, j, k, l):
                    ans = min(ans, get_score(i, j, k, l))

print(ans)
'''