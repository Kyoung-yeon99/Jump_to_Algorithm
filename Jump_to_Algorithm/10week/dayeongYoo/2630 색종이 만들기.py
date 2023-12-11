# n:색종이 크기
n = int(input())
# 색종이 색깔 - 0: 하얀색, 1: 파란색
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))


# 색깔 탐색
def color(x, y, n):
    total = 0  # 색깔 카운트
    for i in range(x, x + n):
        for j in range(y, y + n):
            total += paper[i][j]
    if total == 0:  # 하얀색
        return 0
    elif total == n ** 2:  # 파란색
        return 1
    else:  # 섞임
        return -1


# 색깔 개수 카운트
w, b = 0, 0


# 색종이 분할 정복
def cut(x, y, n):
    q = color(x, y, n)
    if q == -1:  # 섞였을 경우
        cut(x, y, n // 2)  # 문제에서의 I 사분면
        cut(x + n // 2, y, n // 2)
        cut(x, y + n // 2, n // 2)
        cut(x + n // 2, y + n // 2, n // 2)
    elif q == 0:  # 하얀색
        global w
        w += 1
        return
    else:  # 파란색
        global b
        b += 1
        return


cut(0, 0, n)
print(w)
print(b)
