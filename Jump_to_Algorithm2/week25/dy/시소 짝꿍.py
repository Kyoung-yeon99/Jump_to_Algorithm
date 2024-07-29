# 중심으로부터 2, 3, 4m에 좌석
# 탑승한 사람의 무게 = 시소 축과 좌석 간의 거리의 곱
# 몇쌍?
from collections import Counter


def solution(weights):
    answer = 0
    # 몸무게 빈도 저장 -> 중복 처리
    weight_count = Counter(weights)

    # 시소 좌석 간 거리 비율
    distances = [2, 3, 4]

    # 같은 몸무게끼리의 쌍 계산
    for weight in weight_count:
        if weight_count[weight] > 1:
            answer += weight_count[weight] * (weight_count[weight] - 1) // 2

    # 다른 거리 좌석 간의 몸무게 쌍 계산
    for i in range(len(distances)):
        for j in range(i + 1, len(distances)):
            for weight in weight_count:
                pair_weight = weight * distances[j] / distances[i]
                if pair_weight in weight_count:
                    answer += weight_count[weight] * weight_count[pair_weight]

    return answer