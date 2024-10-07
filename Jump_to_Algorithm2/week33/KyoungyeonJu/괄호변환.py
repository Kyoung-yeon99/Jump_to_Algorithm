def solution(p):
    # 올바른 문자열인지 확인
    def is_right(pp):
        left, RIGHT = [], True
        for i in pp:
            if i == '(':  # 여는 괄호이면
                left.append('(')
            else:  # 닫는 괄호이면
                if left:  # 리스트가 비어 있지 않으면
                    left.pop()
                else:
                    RIGHT = False
                    break

        if RIGHT and not left:  # 올바르고 리스트가 비어 있으면
            return True

        return False


    # 문자열 w를 u,v로 분리
    def separate(w):
        u, v = '', ''
        open, close = 0, 0
        for i in range(len(w)):
            ii = w[i]
            if ii == '(':
                open += 1
            else:
                close += 1

            if open == close:
                u = w[:i + 1]
                v = w[i + 1:]
                break

        return u, v

    # 괄호 방향 뒤집기
    def reverse(s):
        r = {"(": ")", ")": "("}
        rr = [r[i] for i in s]
        return ''.join(rr)


    def check(w):
        if w == '':  # 빈 문자열인 경우, 빈 문자열 반환
            return ''

        u, v = separate(w)
        if is_right(u):
            return u + check(v)
        else:
            return '('+check(v)+')'+reverse(u[1:-1])

    # 일단 먼저 올바른 문자열인지 확인
    if is_right(p):
        return p

    return check(p)
