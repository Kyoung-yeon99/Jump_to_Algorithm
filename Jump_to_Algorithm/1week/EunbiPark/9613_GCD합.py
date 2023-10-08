# 가능한 모든 쌍의 GCD 합 출력
# GCD는 두 수로 만드는 것

n = int(input())

for _ in range(n):
    ret = 0
    nums = (list(map(int, input().split())))
    cnt = nums.pop(0)

    nums.sort()

    for i in range(len(nums) -1):
        for j in range(i + 1, len(nums)):
            # 이 두 조합으로 GCD 구하기
            for k in range(nums[i], 0, -1):
                if nums[i] % k == 0 and nums[j] % k == 0:
                    ret += k
                    break
    print(ret)





