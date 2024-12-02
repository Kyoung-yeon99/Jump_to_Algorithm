H, W = map(int, input().split())
heights = list(map(int, input().split()))

if not heights:
    print(0)

answer = 0
n = len(heights)
left_max = [0] * n
right_max = [0] * n

# 왼쪽 최대 높이 계산
left_max[0] = heights[0]
for i in range(1, n):
    left_max[i] = max(left_max[i - 1], heights[i])

# 오른쪽 최대 높이 계산
right_max[n - 1] = heights[n - 1]
for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], heights[i])

# 고이는 물의 양 계산
for i in range(n):
    trapped = min(left_max[i], right_max[i]) - heights[i]
    if trapped > 0:
        answer += trapped

print(answer)