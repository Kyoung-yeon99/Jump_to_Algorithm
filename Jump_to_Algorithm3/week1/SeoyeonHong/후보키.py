# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations

# 후보 키의 최대 개수
def solution(relation):
    R = len(relation)
    C = len(relation[0])
    
    candidates = [] # 모든 속성 조합
    for i in range(1, C+1):
        candidates.extend(combinations(range(C), i))
    
    # 유일성 검사
    unique_keys = []
    for candidate in candidates:
        tuples = set()
        for r in range(R):
            tuples.add(tuple(relation[r][c] for c in candidate))
        if len(tuples) == R:
            unique_keys.append(candidate)
    
    # 최소성 검사
    candidate_keys = []
    for keys in unique_keys:
        if len(keys) == 1:
            candidate_keys.append(keys)
            continue
        
        possible = True
        for ck in candidate_keys:
            if set(ck).issubset(keys):
                possible = False
                break
        if possible:
            candidate_keys.append(keys)
                    
    return len(candidate_keys)