N = int(input())
star = [[" " for _ in range(N)] for _ in range(N)]


def draw_star(x, y, n):
    print("x=",x,"y=",y,"n=",n)
    if n == 1:
        star[x][y] = "*"
        return

    tri = n//3
    draw_star(x, y, tri)  # 0
    draw_star(x, y+tri, tri)  # 1
    draw_star(x, y+tri*2, tri)  # 2
    draw_star(x+tri, y, tri)  # 3, 4번은 정중앙 공백으로 비워둠
    draw_star(x+tri, y+tri*2, tri)  # 5
    draw_star(x+tri*2, y, tri)  # 6
    draw_star(x+tri*2, y+tri, tri)  # 7
    draw_star(x+tri*2, y+tri*2, tri)  # 8
    return


draw_star(0, 0, N)
for i in range(N):
    print("".join(map(str, star[i])))
