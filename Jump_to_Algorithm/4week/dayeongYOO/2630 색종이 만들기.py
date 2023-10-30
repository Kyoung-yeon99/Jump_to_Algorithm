# 입력
n = int(input())
paper = []
ans = [0, 0]

for _ in range(n):
    paper.append(list(map(int, input().split())))


def dividePaper(x, y, n):
    color = paper[x][y]

    for row in range(x, x + n):
        for col in range(y, y + n):
            if color != paper[row][col]:
                dividePaper(x, y, n // 2)  # 1
                dividePaper(x, y + n // 2, n // 2)  # 2
                dividePaper(x + n // 2, y, n // 2)  # 3
                dividePaper(x + n // 2, y + n // 2, n // 2)  # 4
                return
                # 모든 범위 내 같은 색종이라면
    if color == 0:
        ans[0] += 1  # 하얀색
    else:
        ans[1] += 1  # 파란색


# 실행
dividePaper(0, 0, n)

# 출력
for a in ans:
    print(a)
