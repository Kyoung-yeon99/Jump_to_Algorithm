# https://school.programmers.co.kr/learn/courses/30/lessons/138476

# 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을
from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    tangerine_num = 0
    nums = sorted(counter.values(), key= lambda x: -x) # 크기별 개수를 내림차순으로 정렬
    
    for num in nums:
        tangerine_num += num
        answer += 1
        if tangerine_num >= k:
            break
    
    return answer