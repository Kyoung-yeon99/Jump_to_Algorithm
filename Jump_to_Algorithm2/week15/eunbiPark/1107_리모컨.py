n = int(input())
m = int(input())

if m:
    nums = tuple(input().split()) # 문자열로 받기
else:
    nums = ()

ans = abs(100 - n)
for num in range(1000001):
    for s_num in str(num):
        if s_num in nums: # 고장난 번호
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - n))

print(ans)