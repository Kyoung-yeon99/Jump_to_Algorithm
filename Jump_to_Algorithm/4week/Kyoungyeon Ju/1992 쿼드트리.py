import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().strip())) for _ in range(N)]
result = []


def quad_tree(x, y, n):
    number = matrix[x][y]  # 압축 비교 기준
    #print("x=", x, "y=", y, "n=", n, "number=", number)
    for i in range(x, x+n):
        for j in range(y, y+n):
            #print("i=", i, "j=", j)
            if number != matrix[i][j]:  # 압축 불가능이면
                half = n//2
                result.append("(")
                #print("number=", number, "matrix[i][j]", matrix[i][j], "result", result)
                quad_tree(x, y, half)  # 왼쪽 위
                quad_tree(x, y+half, half)  # 오른쪽 위
                quad_tree(x+half, y, half)  # 왼쪽 아래
                quad_tree(x+half, y+half, half)  # 오른쪽 아래
                result.append(")")
                #print("result", result)
                return

    # 압축 가능하면
    if number == 0:
        result.append(0)
        #print("result", result)
    else:
        result.append(1)
        #print("result", result)


quad_tree(0, 0, N)
print("".join(map(str, result)))
