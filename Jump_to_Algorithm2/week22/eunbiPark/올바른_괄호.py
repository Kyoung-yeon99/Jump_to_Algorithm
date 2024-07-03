def solution(s):
    stack = []
    for a in s:
        if a == '(':
            stack.append(a)
        elif len(stack) and a == ')':
            stack.pop()
        else: # stack이 비어 있으면서 ')'를 만나면
            return False

    return False if len(stack) else True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))