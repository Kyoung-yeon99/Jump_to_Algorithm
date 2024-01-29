n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

def recur(x_start, y_start, n):
    # 영역 모두 같은 숫자인지
    check = arr[x_start][y_start]
    same = True
    for i in range(x_start, x_start+n):
        for j in range(y_start, y_start+n):
            if arr[i][j] != check:
                same=False
                break

    if not same:

        print("(", end='')
        # 왼쪽 위
        recur(x_start, y_start, n//2)

        # 오른쪽 위
        recur(x_start, y_start + n//2, n//2)

        # 왼쪽 아래
        recur(x_start + n//2, y_start, n//2)

        # 오른쪽 아래
        recur(x_start + n//2, y_start + n//2 , n//2)
        print(")", end='')


    if same:
        if check==1:
            print(1, end='')
        else:
            print(0, end='')


recur(0, 0, n)
