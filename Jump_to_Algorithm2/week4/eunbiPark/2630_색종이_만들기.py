# 정사각형의 하얀색, 파란색 종이 만들기
# 같은 색으로 칠해져 있지 않으면 같은 크기의 4개의 색종이로 나눈다
# 하나의 정사각형이 되어 더 이상 자를 수 없을 때 까지 반복
# 하얀색(0), 파란색(1) 색종이의 개수 출력

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0

def dfs(x, y, n):
    global blue, white
    check = paper[x][y]
    # 같은 색상인지 확인
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                check = -1
                break

    # 중간에 다른 색이 섞여 있다면 -> 분할
    if check == -1:
        n //= 2
        dfs(x, y, n)
        dfs(x, y + n, n)
        dfs(x + n, y, n)
        dfs(x + n, y + n, n)


    elif check == 0: # 흰색이면
        white += 1

    else:
        blue += 1

dfs(0, 0, n)
print(white)
print(blue)