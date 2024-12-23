n = int(input())
nums = list(map(int, input().split()))
res=0
nums.sort()
for i in range(n):
    temp = nums[:i] + nums[i+1:]
    start, end = 0, len(temp)-1
    # end = i-1
    while start < end:
        total = temp[start]+temp[end]
        if total==nums[i]:
            res+=1
            break
        if total<nums[i]:
            start+=1
        else:
            end -= 1
print(res)
