# https://school.programmers.co.kr/learn/courses/30/lessons/135807

import math
from functools import reduce

def solution(arrayA, arrayB):
    answer = 0
    gcdA = reduce(math.gcd, arrayA) # arrayA의 최대공약수
    gcdB = reduce(math.gcd, arrayB) # arrayB의 최대공약수
    
    if not divided(gcdA, arrayB): # arrayB가 arrayA의 최대공약수로 나누어지지 않을 경우
        answer = max(answer, gcdA)
    if not divided(gcdB, arrayA): # arrayA가 arrayB의 최대공약수로 나누어지지 않을 경우
        answer = max(answer, gcdB) 
    return answer # 두 최대공약수가 조건을 만족하지 않을 경우 0 반환
    
def divided(gcd, array): # array 배열의 숫자들이 gcd로 나누어떨어지는지 확인
    if gcd == 1:
        return True
    for num in array:
        if num % gcd == 0:
            return True
    return False