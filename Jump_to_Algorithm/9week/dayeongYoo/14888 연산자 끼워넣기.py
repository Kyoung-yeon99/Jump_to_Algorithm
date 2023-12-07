from itertools import permutations

n = int(input())
operands = list(map(int, input().split()))  # 피연산자
op_cnt = list(map(int, input().split()))  # 연산자 개수
op_type = ['+', '-', '*', '/']  # 연산자 종류
operators = []  # 연산자 저장 리스트
max_v = -1000000000  # 최대값 초기화: -10억
min_v = 1000000000  # 최소값 초기화: +10억

# 1. 연산자 구하기
for i in range(4):  # 연산자
    for _ in range(op_cnt[i]):
        operators.append(op_type[i])  # 연산자 저장


# 2. 계산
def cal(op):
    ans = operands[0]  # 피연산자 초기화
    for j in range(0, len(op)):
        if op[j] == '+':
            ans += operands[j + 1]
        elif op[j] == '-':
            ans -= operands[j + 1]
        elif op[j] == '*':
            ans *= operands[j + 1]
        elif op[j] == '/':
            if ans < 0 and operands[j + 1] > 0:  # 음수를 양수로 나눌 때는
                ans = -((-ans) // operands[j + 1])  # 양수로 바꾼후 몫을 취하고, 그 몫을 양수로 바꾼다.
            else:
                ans //= operands[j + 1]
    return ans


for op in list(permutations(operators, len(operators))):  # 순열
    val = cal(op)
    max_v = max(val, max_v)
    min_v = min(val, min_v)
print(max_v)
print(min_v)
