def solution(s):
    answer = 0
    l = len(s)
    arr = list(s)

    for i in range(l):
        narr = []  # 스택
        Flag = True  # 올바른 괄호 문자열인지 확인
        for j in arr:
            if j == '(' or j == '[' or j == '{':  # 열리는 괄호
                narr.append(j)
            else:  # 닫히는 괄호
                if len(narr) == 0:  # 스택 empty인 경우, False
                    Flag = False

                elif j == ')':
                    if narr.pop() == '(': continue
                    else: Flag = False
                elif j == '}':
                    if narr.pop() == '{': continue
                    else: Flag = False
                elif j == ']':
                    if narr.pop() == '[': continue
                    else: Flag = False

            if Flag is False:
                break

        if Flag and not narr:  # 올바른 괄호 문자열이면서 빈 스택이면, 테케13 "(){{"
            answer += 1

        # 문자열 회전
        front = arr.pop(0)
        arr.append(front)

    return answer


"""
"[](){}"	3
"}]()[{"	2
"[)(]"	0
"}}}"	0
"(){{"
"""