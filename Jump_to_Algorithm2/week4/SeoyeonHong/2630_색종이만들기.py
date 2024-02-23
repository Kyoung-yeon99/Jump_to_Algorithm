import sys

white = 0
blue = 0

def divide(size, row, column):
    global white, blue
    if size == 2:
        colors = nums[row][column] + nums[row][column+1] + nums[row+1][column] + nums[row+1][column+1]
    else: 
        size = size // 2
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

for r in result:
    if r == '0':
        white += 1
    elif r == '1':
        blue += 1

print(white)
print(blue)