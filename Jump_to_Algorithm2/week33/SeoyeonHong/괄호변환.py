# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def right_string(str):
    cnt = 0
    for s in str:
        if s == '(':
            cnt += 1
        else:
            if cnt > 0:
                cnt -= 1
            else: # 닫는 괄호의 짝이 맞지 않는다면
                return False
    return cnt == 0

def split_string(p): # 2단계
    if not p: # p가 빈 문자열일 경우 빈 문자열 반환
        return ''
    
    u, v = '', '' # 두 "균형잡힌 괄호 문자열"
    for i in range(2, len(p)+1, 2): # 짝수의 길이를 가지는 문자열 확인
        u = p[:i]
        if u.count('(') == u.count(')'): # u를 "균형잡힌 괄호 문자열"로 더 분리할 수 없을 경우
            v = p[i:]
            break

    if right_string(u): # u가 "올바른 괄호 문자열"이라면
        return u + split_string(v) # v에 대해 1단계부터 다시 수행한 결과 문자열을 u에 이어 붙여 반환
    else: # u가 "올바른 괄호 문자열"이 아니라면 4단계 수행
        str = '(' + split_string(v) + ')' # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 괄호로 감싼다
        u = ''.join(')' if c == '(' else '(' for c in u[1:-1]) # u의 앞뒤 문자를 제거하고 괄호 방향을 뒤집는다
        return str + u

def solution(p):
    answer = p
    if p and not right_string(p): # 빈 문자열이 아니고 "올바른 괄호 문자열"이 아닐 경우
        answer = split_string(p)
    return answer
