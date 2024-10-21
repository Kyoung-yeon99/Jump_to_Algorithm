# https://school.programmers.co.kr/learn/courses/30/lessons/42839

# 만들 수 있는 소수의 개수
from itertools import permutations
import math

def is_prime(num): # 소수 판별
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
        
    return True
    
def solution(numbers):
    answer = 0
    new_numbers = [] # 종이 조각을 조합해서 만든 수
    
    for i in range(1, len(numbers)+1):
        new_numbers.extend(permutations(numbers, i)) # 만들 수 있는 조합 추가
        
    new_numbers = list(set(new_numbers)) # 중복되는 조합 제거
    
    for i in range(len(new_numbers)):
        new_numbers[i] = int(''.join(new_numbers[i])) # 숫자로 변환
        
    for num in set(new_numbers):
        if is_prime(num): # 소수인지 확인
            answer += 1
            
    return answer