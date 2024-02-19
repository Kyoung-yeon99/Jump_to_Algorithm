def make_paper(x, y, m):
    global white, blue

    a = paper[x][y]  # 가장 첫번째 칸의 색

    for i in range(x, x+m):
        for j in range(y, y+m):
            if a != paper[i][j]:  # 모두 같은 색으로 칠해져 있지 않으면
                half = m//2
                make_paper(x, y, half)  # 왼위
                make_paper(x, y+half, half)  # 오위
                make_paper(x+half, y, half)  # 왼아래
                make_paper(x+half, y+half, half)  # 오아래
                return

   # 모두 같은 색으로 칠해져 있다면
    if a == 0:
        white += 1
    else:
        blue += 1


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0
make_paper(0, 0, n)
print(f"{white}\n{blue}")
