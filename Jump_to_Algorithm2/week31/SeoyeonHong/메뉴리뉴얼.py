# https://school.programmers.co.kr/learn/courses/30/lessons/72411?language=python3

from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for k in course: # 요리 k개 코스
        candidates = [] # 코스요리 메뉴 구성 후보
        for menu_li in orders: # 각 주문에 대해
            for li in combinations(menu_li, k): # len(menu_li) < k 일 경우 [] 반환
                res = ''.join(sorted(li)) # 문자열 생성
                candidates.append(res) # 후보에 추가
        sorted_candidates = Counter(candidates).most_common() # 가장 많이 함께 주문된 순으로 정렬
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]] # 2명 이상이 주문하고 가장 많이 주문된 구성만 추가
            
    return sorted(answer)