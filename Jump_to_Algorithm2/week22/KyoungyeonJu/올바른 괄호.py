def solution(s):
    a = []
    for i in range(len(s)):
        if s[i] == '(':
            a.append(s[i])
        elif s[i] == ')':
            if len(a) == 0:
                return False
            else:
                a.pop()

    if len(a) != 0:
        return False

    return True


"""
def solution(s):
    answer = True
    a = []
    for i in range(len(s)):
        if i == 0 and s[i] == ')':
            answer = False
            break
        elif s[i] == '(':
            a.append(s[i])
        else:  #
            if len(a) == 0:
                answer = False
                break
            else:
                a.pop()

    if len(a) != 0:
        answer = False

    return answer
"""