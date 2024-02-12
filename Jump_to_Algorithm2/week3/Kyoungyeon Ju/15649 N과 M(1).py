def per():
    if len(nums) == m:  # 탈출 조건: 배열 길이가 M일 때
        print(*nums)
        return

    for i in range(1, n+1):  # 작은 숫자부터 채우기
        if i not in nums:  # 배열에 없는 숫자이면
            nums.append(i)
            print("append", i)
            per()
            nums.pop()
            print("pop")


# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
n, m = map(int, input().split())
nums = []
com()



"""
# 내장 함수 사용
from itertools import permutations
n, m = map(int, input().split())
p = permutations(range(1, n+1), m)
for i in p:
    print(*i)
"""
