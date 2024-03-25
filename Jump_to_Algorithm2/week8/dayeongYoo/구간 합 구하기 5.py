# 구간 합 구하기
# 생짜로 수열 합하면 시간초과
# 1024*1024*100, 000
# https://velog.io/@ready2start/Python-백준-11660-구간-합-구하기-5

n, m = map(int, input().split())

numbers = [[0] * (n + 1)]

for _ in range(n):
    nums = list(map(int, input().split()))
    nums.insert(0, 0)  # 첫 번째 열에 0 추가
    numbers.append(nums)

# prefix sum 행렬 만들기

# 1. 행 별로 더하기
for i in range(1, n + 1):
    for j in range(1, n):
        numbers[i][j + 1] += numbers[i][j]

# 2. 열 별로 더하기
for j in range(1, n + 1):
    for i in range(1, n):
        numbers[i + 1][j] += numbers[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # (x1, y1)에서 (x2, y2)까지의 합
    # p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1]
    print(numbers[x2][y2] - numbers[x1 - 1][y2] - numbers[x2][y1 - 1] + numbers[x1 - 1][y1 - 1])
