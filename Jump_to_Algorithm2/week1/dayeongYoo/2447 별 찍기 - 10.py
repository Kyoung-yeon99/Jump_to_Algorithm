def star(i, j, n):
    if n == 1:  # 정사각형의 변이라면(N x N 정사각형 크기가 1이라면)
        print("*", end="")
    elif (i // (n // 3)) % 3 == 1 and (j // (n // 3)) % 3 == 1:  # 정사각형의 가운데라면
        print(" ", end="")  # 공백 출력
    else:
        star(i, j, n // 3)  # 정사각형의 크기를 n/3로 줄인 후 정사각형 중간에 위치한 공백인지 재탐색


n = int(input())

# 정사각형이므로 이중 for문
for i in range(n):
    for j in range(n):
        star(i, j, n)
    print()
