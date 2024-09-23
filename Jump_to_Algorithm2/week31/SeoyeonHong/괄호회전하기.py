# https://school.programmers.co.kr/learn/courses/30/lessons/76502?language=python3

from collections import deque

def valid(pl): # 올바른 괄호 문자열인지 확인
    stack1 = pl.copy()
    stack2 = []
    while stack1:
        p = stack1.pop()
        if p == ')' or p == ']' or p == '}': # 닫는 괄호일 경우
            stack2.append(p)
        elif p == '(':
            if stack2 == [] or stack2.pop() != ')':
                return False
        elif p == '[':
            if stack2 == [] or stack2.pop() != ']':
                return False
        elif p == '{':
            if stack2 == [] or stack2.pop() != '}':
                return False
    return True if stack2 == [] else False
            

def solution(s):
    answer = 0
    cnt = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
    
    pl = deque(s)
    
    for p in pl:
        cnt[p] += 1
        
    # 여는 괄호와 닫는 괄호의 개수가 다른 경우 올바른 괄호 문자열을 만들 수 없음
    if cnt['('] != cnt[')'] or cnt['['] != cnt[']'] or cnt['{'] != cnt['}']:
        return 0

    for _ in range(len(s)):
        if valid(pl): # 올바른 괄호 문자열일 경우
            answer += 1
        pl.rotate(-1) # 왼쪽으로 1칸 회전
                  
    return answer