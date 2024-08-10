def solution(k, tangerine):
    nums = {}
    for t in tangerine:
        if t not in nums:
            nums[t] = 1
        else:
            nums[t] += 1
    
    s_nums = sorted(nums, key = lambda x: nums[x], reverse = True)
    
    temp = 0
    for idx, s in enumerate(s_nums):
        temp += nums[s]
        if temp >= k:
            return idx + 1
