# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(': # 여는 괄호일 경우
            count += 1
        else: # 닫는 괄호일 경우
            count -= 1
            
        if count < 0: # 닫는 괄호와 맞는 짝이 없을 경우
            return False

    if count != 0: # 여는 괄호와 맞는 짝이 없을 경우
        return False
        
    return True # 짝이 모두 맞을 경우