import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(int, input().split()))

min_move = abs(100-n)

for i in range(1000001):
    nums = str(i)
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break

        elif j == len(nums) - 1:
            min_move = min(min_move, abs(int(nums) - n) + len(nums))

print(min_move)
