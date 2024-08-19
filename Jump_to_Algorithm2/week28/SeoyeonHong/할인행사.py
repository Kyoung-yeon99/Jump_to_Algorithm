# 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수
from collections import Counter

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - 9):
        satisfied = True # 조건 만족 여부
        counter = Counter(discount[i:i+10]) # 제품별 할인하는 날짜의 개수
        for j in range(len(want)):
            if counter[want[j]] < number[j]:
                satisfied = False
                break
        if satisfied:
            answer += 1
    return answer