import sys

def compress(size, row, column):
    if size == 2: # 2 X 2 정사각형
        coordinates = nums[row][column] + nums[row][column+1] + nums[row+1][column] + nums[row+1][column+1]
    else: # 2 X 2 보다 큰 정사각형
        size = size // 2
        # 4등분한 정사각형 압축
        coordinates = compress(size, row, column) + compress(size, row, column + size) + compress(size, row + size, column) + compress(size, row + size, column + size)

    if coordinates == '0000': # 모두 0일 경우 0 반환
            return '0'
    elif coordinates == '1111': # 모두 1일 경우 1 반환
        return '1'
    else:
        return '(' + str(coordinates) + ')' # 두개의 숫자로 이루어졌을 경우 문자 그대로 반환, '()' 추가

n = int(input())
nums = [[0] * n for _ in range(n)]
result = ""

for i in range(n):
    nums[i] = sys.stdin.readline()

if n == 1:
    result = nums[0][0]
else:
    result = compress(n, 0, 0)

print(result)