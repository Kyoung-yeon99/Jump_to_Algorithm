import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

sort_nums = sorted(set(nums)) # nlogn

# 시간 초과 해결
# 숫자: 크기 인덱스
dic = {sort_nums[i]: i for i in range(len(sort_nums))}

for i in nums:
    print(dic[i], end = ' ')
'''
# 시간 초과 
for n in nums: # 1 000 000
    print(sort_nums.index(n), end = ' ')
'''
