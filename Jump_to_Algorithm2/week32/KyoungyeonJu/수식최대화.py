from itertools import permutations


def solution(expression):
    def calculate(ops, nums):
        operator = ops.pop()
        num2 = nums.pop()
        num1 = nums.pop()
        if operator == '+': return num1+num2
        elif operator == '-': return num1-num2
        elif operator == '*': return num1*num2

    answer = 0
    arr = list(expression)
    operators = []  # 문자열에 포함된 연산자 파악
    for i in ["+", "-", "*"]:
        if i in arr:
            operators.append(i)

    for o in permutations(operators, len(operators)):
        nums = []
        ops = []
        op = dict(zip(o, (3, 2, 1)))

        i = 0
        while i < len(expression):
            if expression[i].isdigit():  # 비연산자인 경우
                num = 0
                while i < len(expression) and expression[i].isdigit():
                    num = num*10 + int(expression[i])
                    i += 1
                nums.append(num)

            else:  # 연산자인 경우
                while ops and op[ops[-1]] >= op[expression[i]]:
                    result = calculate(ops, nums)
                    nums.append(result)
                ops.append(expression[i])
                i += 1

        while ops:
            result = calculate(ops, nums)
            nums.append(result)

        answer = max(answer, abs(nums[0]))

    return answer