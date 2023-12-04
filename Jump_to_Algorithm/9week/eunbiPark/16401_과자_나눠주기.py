m, n = map(int, input().split())
snack = list(map(int, input().split()))

start = 1 # 과자의 길이는 1 이상
end = max(snack)

ret = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    if mid == 0:
        total = 0
        break

    for s in snack:
        if s >= mid:
            total += (s // mid)

    if total >= m:
        start = mid + 1
        ret = mid

    else:
        end = mid - 1

print(ret)


# snack.sort(reverse = True)
#
# while m > len(snack):
#     temp = snack[0]
#     snack.remove(temp)
#     snack.append(temp // 2)
#     snack.append(temp // 2)
#     snack.sort(reverse=True)
#
# print(snack[m-1])

'''
# 반례
3 3
1 1 9 
출력: 3
'''