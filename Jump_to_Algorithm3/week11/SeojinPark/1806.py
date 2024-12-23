n, s = map(int, input().split())
nums = list(map(int,input().split()))

start, end = 0, 0
min_length=n+1
hap = nums[0]

while start <= end:
    if hap >= s:
        if min_length > end-start+1:
            min_length = end-start+1
        hap -= nums[start]
        start += 1
    elif end < n-1:
        end+=1
        hap+=nums[end]
    else:
        hap -= nums[start]
        start += 1


if min_length==n+1:
    print(0)
else:
    print(min_length)
