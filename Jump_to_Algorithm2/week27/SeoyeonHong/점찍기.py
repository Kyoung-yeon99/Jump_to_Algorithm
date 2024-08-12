# https://school.programmers.co.kr/learn/courses/30/lessons/140107

import math

def solution(k, d):
    answer = d // k + 1 # b가 0인 점의 개수
    
    for a in range(d):
        num =  d**2 - a**2 * k**2 # sqrt(num) == x가 a 일 때 원 위의 점의 y 좌표
        
        if num > 0:
            answer += math.floor(math.sqrt(num)) // k
            
    return answer