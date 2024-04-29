n = int(input())
liquid = list(map(int, input().split()))
min_num = float('inf')

left, right = 0, len(liquid) -1
while left < right:
    temp_ret = liquid[left] + liquid[right]

    # 0과의 차이 -> 음 양 구분 없음
    if abs(temp_ret) < min_num:
        ret = (liquid[left], liquid[right])
        min_num = abs(temp_ret)

    if temp_ret < 0:
        left += 1
    elif temp_ret > 0:
        right -= 1
    else:
        break

print(*ret)