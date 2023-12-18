from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

for i in range(1, n + 1):
    comb = list(combinations(nums, i))

    for c in comb:
        if sum(c) == s:
            cnt += 1

print(cnt)

# 다른 풀이
def dfs(idx, sum):
    global cnt

    if idx >= n:
        return
    sum += nums[idx]

    if sum == s:
        cnt += 1

    # 지금 더한 원소 포함 
    dfs(idx + 1, sum)
    # 지금 더한 원소 미포함
    dfs(idx + 1, sum - nums[idx])

cnt = 0
dfs(0, 0)

print(cnt)