# 이분탐색
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 1 ≤ N, M ≤ 10^5
titles, nums = [], []
for _ in range(N):
    title, num = input().split()
    num = int(num)
    if len(nums) == 0 or nums[-1] != num:
        nums.append(num)
        titles.append(title)

for _ in range(M):
    n = int(input())
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right) // 2

        if nums[mid] == n:
            left = mid
            break
        elif nums[mid] > n:
            right = mid - 1
        else:
            left = mid + 1

    print(titles[left])


