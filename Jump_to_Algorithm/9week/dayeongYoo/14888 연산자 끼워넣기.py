from itertools import permutations

n = int(input())
operands = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))
op_type = ['+', '-', '*', '/']
operators = []
max_v = -1000000000  # 10억
min_v = 1000000000

for i in range(4):  # 연산자
    for _ in range(op_cnt[i]):
        operators.append(op_type[i])


def cal(op):
    ans = operands[0]
    for i in range(0, len(op)):
        if op[i] == '+':
            ans += operands[i + 1]
        elif op[i] == '-':
            ans -= operands[i + 1]
        elif op[i] == '*':
            ans *= operands[i + 1]
        elif op[i] == '/':
            if ans < 0 and operands[i + 1] > 0:
                ans = -((-ans) // operands[i + 1])
            else:
                ans //= operands[i + 1]
    return ans


for op in list(permutations(operators, len(operators))):
    val = cal(op)
    max_v = max(val, max_v)
    min_v = min(val, min_v)
print(max_v)
print(min_v)
