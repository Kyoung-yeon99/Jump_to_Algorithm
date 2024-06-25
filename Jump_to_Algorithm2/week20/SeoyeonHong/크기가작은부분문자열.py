# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    length = len(p)
    max_num = int(p)
        
    for i in range(len(t)-length+1):
        if int(t[i:i+length]) <= max_num: # 부분 문자열이 p 이하일 경우
            answer += 1
        
    return answer