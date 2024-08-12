from collections import Counter

def solution(k, tangerine):
    # 서로 다른 종류의 수 최소화
    # 한 상자에 담으려는 개수 k
    # 귤의 크기를 담은 배열 tangerine

    answer = 0
    c = Counter(tangerine)
    v = sorted(c.values(), key=lambda x: -x)

    for i in range(len(tangerine)):
        if k <= 0:
            return i
        k -= v[i]

    return len(tangerine)


"""
# 시간 초과
from collections import Counter

def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine)  # 각 크기의 개수 구하기
    
    while k > 0:
        a = c.most_common(1)
        k -= a[0][1]
        answer += 1
        del c[a[0][0]]
        
    return answer
"""