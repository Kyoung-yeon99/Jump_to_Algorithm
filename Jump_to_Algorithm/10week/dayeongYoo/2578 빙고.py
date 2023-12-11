# 빙고판
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))
# 부르는 수
speak = []
for _ in range(5):
    speak.append(list(map(int, input().split())))
# 나온 수 세는 보드판
bingo = [[0] * 5 for _ in range(5)]


def row():
    res = 0  # 빙고 카운트
    for i in range(5):
        cnt = 0  # 행에서 나온 숫자 카운트
        for j in range(5):
            if bingo[i][j] == 1:
                cnt += 1
        if cnt == 5:
            res += 1
    return res


def col():
    res = 0
    for y in range(5):
        cnt = 0  # 열에서 나온 숫자 카운트
        for x in range(5):
            if bingo[x][y] == 1:
                cnt += 1
        if cnt == 5:
            res += 1
    return res


def dia():
    res = 0
    # 왼 -> 오
    cnt = 0  # 대각선에서 나온 숫자 카운트
    for i in range(5):
        if bingo[i][i] == 1:
            cnt += 1
    if cnt == 5:
        res += 1
    # 오->왼
    cnt = 0  # 대각선에서 나온 숫자 카운트
    for i in range(5):
        if bingo[i][5 - i - 1] == 1:
            cnt += 1
    if cnt == 5:
        res += 1
    return res


ans = 0  # 3개면 빙고
# 부르는 수 횟수 체크
num = 0
for i in range(5):
    for j in range(5):
        s = speak[i][j]
        num += 1
        for k in range(5):
            for l in range(5):
                if s == board[k][l]:
                    bingo[k][l] = 1  # 1로 변경
                    ans = 0  # 3개면 빙고

                    # 행
                    ans += row()
                    # 열
                    ans += col()
                    # 대각선 체크
                    ans += dia()
                    if ans >= 3:
                        print(num)
                        exit()
