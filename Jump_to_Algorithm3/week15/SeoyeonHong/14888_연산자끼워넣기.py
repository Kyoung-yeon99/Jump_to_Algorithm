# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램
N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split())) # +, -, ×, ÷ 의 개수
min_result = int(1e9)
max_result = -int(1e9)

def calculate(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1 * num2
    elif op == 3: # 정수 나눗셈(몫만 취함, 음수를 양수로 나누는 경우 주의)
        return int(num1 / num2)

def make_exression(operators, idx, result): # 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
    global min_result, max_result

    if idx == N: # 수식이 완성되었을 경우
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return
    
    for i in range(4): # 각 연산자에 대해
        if operators[i] > 0: # 연산자가 남아있다면
            operators[i] -= 1
            make_exression(operators.copy(), idx+1, calculate(result, nums[idx], i)) # 해당 연산자 사용, 재귀호출로 식 이어서 만들기
            operators[i] += 1

make_exression(operators.copy(), 1, nums[0])

print(max_result)
print(min_result)