paren_lst = list(input())

# 열린 괄호
open_parentheses_cnt = 0
# 막대기 수
stick_cnt = 0
# 레이저는 적어도 하나 존재할 경우 대비(레이저는 있지만 막대기가 없는 경우)
stack = []
# 괄호 판단
pair = {')': '('}
# 그 전의 괄호 저장
before_par = ''

for par in paren_lst:
    if par == '(':
        stack.append(par)
        open_parentheses_cnt += 1  # 괄호수 +1
    elif stack:  # stack에 값이 있는 경우
        if par == ')':  # 닫힌 괄호일 경우
            open_parentheses_cnt -= 1
        if stack[-1] == pair[par]:  # stack의 맨 위가 여는 괄호일때, 현재 괄호가 닫는 괄호라면 -> 레이저임
            stack.pop()  # stack에서 제거
            # 그 전의 문자열과 짝이 맞는 경우 '('+')'
            if before_par == pair[par]:
                stick_cnt += open_parentheses_cnt
            else:
                stick_cnt += 1
    # 그 전의 문자열을 저장
    before_par = par
print(stick_cnt)
