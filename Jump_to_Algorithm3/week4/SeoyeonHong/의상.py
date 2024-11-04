# https://school.programmers.co.kr/learn/courses/30/lessons/42578

# 서로 다른 옷의 조합의 수
from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_type = defaultdict(int) # 의상 종류별 개수
    
    for c in clothes:
        clothes_type[c[1]] += 1
        
    for t in clothes_type: # 조합 수 계산
        answer *= (clothes_type[t] + 1)
        
    return answer - 1 # 의상을 착용하지 않은 경우 제외