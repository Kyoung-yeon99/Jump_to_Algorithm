def check_paper(x, y, m):
    global paper, white, blue
    first = paper[x][y]
    for i in range(x, x+m):
        for j in range(y, y+m):
            if paper[i][j] != first:
                check_paper(x, y,  m//2)  # 왼쪽 상
                check_paper(x+m//2, y, m//2)  # 오른쪽 상
                check_paper(x, y+m//2, m//2)  # 왼쪽 하
                check_paper(x+m//2, y+m//2, m//2)  # 오른쪽 하
                return

    if first == 0:
        white += 1
    else:
        blue += 1


n = int(input())
paper = []
white, blue = 0, 0

for _ in range(n):
    row = list(map(int, input().split()))
    paper.append(row)

check_paper(0, 0, n)
print(white)
print(blue)
