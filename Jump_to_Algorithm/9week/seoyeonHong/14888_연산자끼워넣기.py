# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
# 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
# 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력
n = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))
min_result, max_result = 10000000000, -10000000000

def calculate(i, res, op):
    global min_result, max_result
    if i < n:
        if op[0] > 0:
            calculate(i+1, res+number[i], [op[0]-1, op[1], op[2], op[3]])
        if op[1] > 0:
            calculate(i+1, res-number[i], [op[0], op[1]-1, op[2], op[3]])
        if op[2] > 0:
            calculate(i+1, res*number[i], [op[0], op[1], op[2]-1, op[3]])
        if op[3] > 0:
            calculate(i+1, int(res/number[i]), [op[0], op[1], op[2], op[3]-1]) # 나눗셈 주의
    else: # 모든 연산자를 썼을 경우 최솟값, 최댓값 갱신
        min_result = min(min_result, res)
        max_result = max(max_result, res)

calculate(1, number[0], operator)
print(max_result)
print(min_result)
