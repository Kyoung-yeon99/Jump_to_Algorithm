# 2 ~ n 까지의 수 중 k 번째 지워진 수 찾기

n, k = map(int, input().split())

nums = [True] * (n + 1)
cnt = 0

for i in range(2, len(nums) + 1):
    for j in range(i, n+1, i):
        if nums[j] == True:
            nums[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                break
