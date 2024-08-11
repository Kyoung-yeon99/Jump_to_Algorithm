# 점이 몇 개 찍히는지 계산
# 두 점 사이의 거리 계산
import math


def solution(k, d):
    answer = 0
    # d를 k로 나눈 몫을 구하여 가능한 a의 최대 값을 구하기
    max_range = d // k

    # 가능한 b 값을 찾기
    for a in range(max_range + 1):
        # 가능한 b의 최대 제곱 값
        max_b_square = (d ** 2) - (a * k) ** 2

        # max_b_square가 음수일 경우, b 값 없음
        if max_b_square < 0:
            continue

        # max_b_square의 제곱근을 구하여 가능한 b의 최대 값 구하기
        max_b = int(math.sqrt(max_b_square)) // k

        # 가능한 모든 b 값 도출
        answer += max_b + 1
    return answer