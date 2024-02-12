def com(start):
    if len(nums) == m:
        print(" ".join(map(str, nums)))
        return

    for i in range(start, n+1):
        nums.append(i)
        com(i+1)
        nums.pop()


# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 오름차순 수열
n, m = map(int, input().split())
nums = []
com(1)