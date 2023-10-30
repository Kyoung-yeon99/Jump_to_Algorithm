import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0


def dac(x, y, n):
    global white, blue, matrix
    color = matrix[x][y]  # 컬러 기준
    #print("x=", x, "y=", y, "n=", n, "color=", color)

    # 색종이 자르기
    for i in range(x, x+n):  # x부터 x+n-1까지
        for j in range(y, y+n):  # y부터 y+n-1까지
            #print("i=",i, "j=", j)
            if color != matrix[i][j]: # 컬러가 다르다면
                half = n//2
                #print("color=", color, "matrix[i][j]=", matrix[i][j], "half=",half)
                dac(x, y, half)  # 1 왼쪽 위
                dac(x, y+half, half)  # 2 오른쪽 위
                dac(x+half, y, half)  # 3 왼쪽 아래
                dac(x+half, y+half, half)  # 4 오른쪽 아래
                return

    # 컬러가 같다면
    if color == 0:
        white += 1
    else:
        blue += 1


dac(0, 0, N)
print(white)
print(blue)

