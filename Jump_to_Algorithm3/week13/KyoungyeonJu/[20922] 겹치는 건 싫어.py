import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # 1 <= N <= 200000, 1 <= k <= 100
answer = 0
list = list(map(int, input().split()))
nums = [0]*100001

l, r = 0, 0
while l <= r and r < N:
    nums[list[r]] += 1

    if nums[list[r]] > K:
        while nums[list[r]] > K and l <= r:
            nums[list[l]] -= 1
            l += 1

    r += 1
    answer = max(answer, (r-l))

print(answer)
