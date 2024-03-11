import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
temp = []

for i in range(0, n):
    cnt = 0
    for j in range(nums[i], nums[i] + 5):
        if j not in nums:
            cnt += 1
    temp.append(cnt)
print(min(temp))
