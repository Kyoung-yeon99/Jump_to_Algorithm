def is_balanced(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return True
    return False


def is_correct(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return len(stack) == 0


def solution(p):
    # 빈 문자열이면 빈 문자열 반환
    if p == '':
        return ''

    #문자열을 u, v로 분리
    u, v = '', ''
    for i in range(2, len(p) + 1, 2):
        if is_balanced(p[:i]):
            u = p[:i]
            v = p[i:]
            break

    # u가 올바른 괄호 문자열인지 확인
    if is_correct(u):
        #  v에 대해 재귀적으로 처리
        return u + solution(v)
    else:
        # u가 올바르지 않다면
        result = '('  # '('를 추가
        result += solution(v)  #. v에 대해 재귀적으로 처리한 결과 추가
        result += ')'  # ')'를 추가

        #. u의 첫 번째와 마지막 문자를 제거하고 괄호 방향을 뒤집어서 추가
        u = u[1:-1]  # 첫 번째와 마지막 문자 제거
        u = ''.join(['(' if char == ')' else ')' for char in u])  # 괄호 방향 뒤집기
        result += u

        return result


print(solution("(()())()"))  # "(()())()"
print(solution(")("))  # "()"
print(solution("()))((()"))  # "()(())()"