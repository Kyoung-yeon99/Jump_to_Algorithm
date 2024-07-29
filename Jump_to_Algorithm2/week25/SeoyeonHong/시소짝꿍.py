# https://school.programmers.co.kr/learn/courses/30/lessons/152996

# 탑승한 사람의 무게와 시소 축과 좌석 간의 거리의 곱이 양쪽 다 같은 시소 짝꿍
from collections import defaultdict

def solution(weights):
    answer = 0

    weights_dict = defaultdict(float)
    ratio = [1/1, 1/2, 2/1, 2/3, 3/2, 3/4, 4/3]
    
    for w in weights:
        for r in ratio:
            answer += weights_dict[r * w]
        weights_dict[w] += 1

    return int(answer)