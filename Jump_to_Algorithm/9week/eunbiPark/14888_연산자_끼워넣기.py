n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maximum = -1e9
minimum = 1e9

def dfs(i, total, add, sub, mul, div):
    global maximum, minimum

    # 종료 조건
    if i == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # dfs
    # if - elif 로 받으면 안된다 ...
    if add > 0:
        dfs(i + 1, total + nums[i], add - 1, sub, mul, div)
    if sub > 0:
        dfs(i + 1, total - nums[i], add, sub - 1, mul, div)
    if mul > 0:
        dfs(i + 1, total * nums[i], add, sub, mul - 1, div)
    if div > 0:
        dfs(i + 1, int(total / nums[i]), add, sub, mul, div - 1)

# main
dfs(1, nums[0], add, sub, mul, div)
print(maximum)
print(minimum)

'''
# 시간 초과 
from itertools import permutations
n = int(input())
nums = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())

op = ['+'] * plus + ['-'] * minus + ['*'] * multiple + ['/'] * divide

op_list = list(permutations(op, len(op)))
ret = []

for o in op_list:
    temp_ret = nums[0]
    for i in range(len(op)):
        if o[i] == '+':
            temp_ret += nums[i + 1]
        elif o[i] == '-':
            temp_ret -= nums[i + 1]
        elif o[i] == '*':
            temp_ret *= nums[i + 1]
        elif o[i] == '/':
            if temp_ret < 0:
                temp_ret = -temp_ret
                temp_ret //= nums[i + 1]
                temp_ret = -temp_ret
            else:
                temp_ret //= nums[i + 1]
    ret.append(temp_ret)

print(max(ret))
print(min(ret))
'''