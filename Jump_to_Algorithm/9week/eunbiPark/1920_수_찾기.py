import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())
find = list(map(int, input().split()))

def binary(num):
    start = 0
    end = n-1

    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == num:
            return True
        if num < nums[mid]:
            end = mid - 1
        elif num > nums[mid]:
            start = mid + 1

for i in range(m):
    if binary(find[i]):
        print(1)
    else:
        print(0)