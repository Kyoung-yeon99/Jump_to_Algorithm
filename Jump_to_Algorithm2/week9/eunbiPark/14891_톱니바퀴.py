chair = [list(map(int, input())) for _ in range(4)]
k = int(input())


# 시계 회전
def turn_right(n):
    temp_chair[n].insert(0, temp_chair[n].pop())


# 반시계 회전
def turn_left(n):
    temp_chair[n].append(temp_chair[n].pop(0))


# 의자 확인 후 값이 같으면 True
def check(n, direction, compare):
    # 범위 확인
    if n < 0 or n > 3:
        return False

    if direction == 'L':
        if compare != chair[n][2]:  # 인덱스 2
            return True  # 회전

    else:
        if compare != chair[n][6]:  # 인덱스 6
            return True

    return False


def move(n, d):
    if turn[n]:
        return

        # 1. 들어온 대로 회전
    if d == 1:  # 시계
        turn_right(n)
    else:  # 반시계
        turn_left(n)

    turn[n] = True

    # 2. 인접 좌석 확인
    if check(n - 1, 'L', chair[n][6]):
        move(n - 1, -d)
    if check(n + 1, 'R', chair[n][2]):
        move(n + 1, -d)


def calc():
    ans = 0
    for idx, c in enumerate(chair):
        ans += ((2 ** idx) * c[0])
    return ans


# main
for _ in range(k):
    # 의자 번호, 회전 방향
    n, d = map(int, input().split())
    n -= 1
    temp_chair = [[0] * 8 for _ in range(4)]

    for i in range(4):
        for j in range(8):
            temp_chair[i][j] = chair[i][j]

    # 회전 확인 테이블
    turn = [False] * 4

    # 인자 값대로 움직이기 - 연속 움직임까지 처리
    move(n, d)

    for i in range(4):
        for j in range(8):
            chair[i][j] = temp_chair[i][j]

# 결과 계산
ans = calc()
print(ans)