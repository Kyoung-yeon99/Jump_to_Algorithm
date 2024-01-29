import sys

def compress(size, row, column):
    if size == 2: # 2 X 2 정사각형
        coordinates = nums[row][column] + nums[row][column+1] + nums[row+1][column] + nums[row+1][column+1]
    else: # 2 X 2 보다 큰 정사각형
        size = size // 2
        # 4등분한 정사각형 압축
        coordinates = compress(size, row, column) + compress(size, row, column + size) + compress(size, row + size, column) + compress(size, row + size, column + size)

    if coordinates == '0000':
            return '0'
    elif coordinates == '1111':
        return '1'
    else:
        return '(' + str(coordinates) + ')'

n = int(input())
nums = [[0] * n for _ in range(n)] # n x n 크기의 배열, 0으로 초기화
result = ""

for i in range(n):
    nums[i] = sys.stdin.readline()

if n == 1: # 영상의 크기가 1일 경우 압축X 
    result = nums[0][0]
else:
    result = compress(n, 0, 0)

print(result)