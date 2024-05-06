import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
min_dif = int(2e9)
left, right = 0, n-1
answer_left, answer_right = -min_dif, min_dif

while left < right:
    num = abs(nums[left] + nums[right])
    if num < min_dif:
        min_dif = num
        answer_left, answer_right = nums[left], nums[right]

    if nums[left] + nums[right] < 0:  # 알카리성이 크면
        left += 1
    else:  # 산성이 크면
        right -= 1

print(answer_left, answer_right)