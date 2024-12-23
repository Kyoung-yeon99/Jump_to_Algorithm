n = int(input())
nums = sorted(list(map(int, input().split())))
GOOD = 0

for i in range(n):
    target = nums[i]

    left = 0
    right = n-1
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        sum = nums[left]+nums[right]
        if sum == target:
            GOOD += 1
            break
        elif sum > target:
            right -= 1
        else:
            left += 1

print(GOOD)
