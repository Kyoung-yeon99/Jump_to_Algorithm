N = int(input())
screen = []
result = []
for _ in range(N):
    row = input()  # 띄어쓰기 없는 숫자들 str 문자열로 입력받기
    screen.append(list(map(int, row)))  # map(int, 문자열)


def quad_tree(x, y, n):
    a = screen[x][y]  # 압축 비교 기준
    for i in range(x, x+n):  # 세로
        for j in range(y, y+n):  # 가로
            if screen[i][j] != a:  # 압축 불가능
                half = n//2
                result.append("(")
                quad_tree(x, y, half)  # 왼위
                quad_tree(x, y+half, half)  # 오위
                quad_tree(x+half, y, half)  # 왼아래
                quad_tree(x+half, y+half, half)  #오아래
                result.append(")")
                return  # 없다면, 계속해서 4개의 작은 영역 탐색. 압축 불가능한 경우에도 해당 부분 처리 후 함수 종료 필요.

    # 압축 가능
    result.append(a)


quad_tree(0, 0, N)
print("".join(map(str, result)))
