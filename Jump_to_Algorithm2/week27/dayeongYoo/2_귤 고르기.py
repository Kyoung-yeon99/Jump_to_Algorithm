# 귤 중 k개를 골라 상자에 담기
# k: 판매할 귤 개수
# 귤을 크기별 분류 -> 서로 다른 종류의 수를 최소화
from collections import Counter


def solution(k, tangerine):
    # 뽑은 귤 종류
    answer = 0

    # 귤 빈도수 계산
    counter = Counter(tangerine)

    # 빈도수 내림차순 정렬
    frequencies = sorted(counter.values(), reverse=True)

    # 귤 뽑기
    tan_cnt = 0  # 뽑은 귤 개수
    for freq in frequencies:
        tan_cnt += freq
        answer += 1
        if tan_cnt >= k:
            break
    return answer