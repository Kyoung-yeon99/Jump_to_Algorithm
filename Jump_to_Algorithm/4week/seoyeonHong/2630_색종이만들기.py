import sys

white = 0
blue = 0

# 쿼드 트리 응용
def divide(size, row, column):
    global white, blue
    if size == 2: # 2 X 2 정사각형
        colors = nums[row][column] + nums[row][column+1] + nums[row+1][column] + nums[row+1][column+1]
    else: # 2 X 2 보다 큰 정사각형
        size = size // 2
        # 4등분한 정사각형 압축
        colors = divide(size, row, column) + divide(size, row, column + size) + divide(size, row + size, column) + divide(size, row + size, column + size)

    if colors == '0000':
        return '0'
    elif colors == '1111':
        return '1'
    else:
        return colors

n = int(input())
nums = [[0] * n for _ in range(n)]
result = ""

for i in range(n):
    nums[i] = sys.stdin.readline().split()

result = divide(n, 0, 0)

# 0과 1의 개수만큼 하얀색 색종이 개수와 파란색 색종이 개수 존재
for r in result:
    if r == '0':
        white += 1
    elif r == '1':
        blue += 1

print(white)
print(blue)