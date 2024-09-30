# https://school.programmers.co.kr/learn/courses/30/lessons/67257?language=python3

# 연산자의 우선순위 재정의
# 주의 - 절댓값 사용
from itertools import permutations
import re

def solution(expression):
    max_num = 0 # 상금의 최댓값
    operators = ['+', '-', '*'] # 연산자
    exp = re.split(r'(\+|-|\*)', expression) # 피연산자, 연산자가 구분된 리스트 생성
    for operator in list(permutations(operators)): # 각 연산자 우선순위 조합에 대해
        new_exp = exp.copy() 
        for i in range(3): # 우선순위에 따라 연산 계산
            stack = [] # 연산 계산을 위한 스택
            j = 0
            while j < len(new_exp):
                if new_exp[j] == operator[i]: # i번째 우선순위인 연산자일 경우
                    operand1 = stack.pop() # 피연산자1
                    operand2 = new_exp[j+1] # 피연산자2
                    stack.append(str(eval(operand1+new_exp[j]+operand2))) # 스택에 계산 결과 추가
                    j += 1 # 피연산자의 인덱스 건너뛰기
                else:
                    stack.append(new_exp[j]) # 피연산자 또는 우선순위가 낮은 연산자일 경우 스택에 추가
                j += 1
            new_exp = stack.copy()
        max_num = max(max_num, abs(sum(list(map(int, new_exp))))) # 상금 최댓값 갱신
    
    return max_num