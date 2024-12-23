# 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있는지
# 0 <= heights[i] <= n-i

n = int(input())  # 1 <= n <= 10
heights = list(map(int, input().split()))
order = [0]*n

for i in range(n):
    num = heights[i]
    if i == 0:
        order[num] = i+1
    else:
        cnt_zero = 0
        for j in range(n):
            if order[j] == 0:
                if cnt_zero == num:
                    order[j] = i + 1
                    break
                else:
                    cnt_zero += 1

print(*order)
