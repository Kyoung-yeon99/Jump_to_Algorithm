# 0: 빈칸, 1: 사람, 2: 병원
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
people = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if board[i][j] == 1
]
hospital = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if board[i][j] == 2
]


def calc(x, y):
    temp = float('inf')
    # 병원 거리의 최소 값을 찾기 
    for k in choice:
        gx, gy = hospital[k]
        temp = min(temp, abs(x - gx) + abs(y - gy))
    return temp


ans = float('inf')


def make_sum():
    total = 0
    # 모든 사람의 최소 병원을 찾아 합 구하기 
    for person in people:
        x, y = person
        total += calc(x, y)
    return total


# 1. 남길 병원 선택하기
choice = []


def choose(idx, num):
    global ans
    if num == m:
        # 2. 병원 거리의 합 구하기 
        ans = min(ans, make_sum())

        return

    for i in range(idx, len(hospital)):
        choice.append(i)
        choose(i + 1, num + 1)
        choice.pop()


choose(0, 0)
print(ans)