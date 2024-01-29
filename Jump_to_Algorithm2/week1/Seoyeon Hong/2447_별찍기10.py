n = int(input()) # 3의 거듭제곱
ans = [[' ' for _ in range(n)] for _ in range(n)] # n x n 크기의 배열, 공백 문자로 초기화

def checkStar(size, row, column): # 별이 들어가는 위치 반영
    if size == 1:
        ans[row][column] = '*'
    else:
        size //= 3
        for i in range(3):
            for j in range(3):
                if i % 3 == 1 and j % 3 == 1: # 가운데는 공백으로 유지
                    continue
                else:
                    checkStar(size, row + i * size, column + j * size)
            
checkStar(n, 0, 0)
for row in ans:
    for column in row:
        print(column, end='')
    print()