from math import isqrt, sqrt, ceil


def solution(r1, r2):
    answer = 0

    # 원의 대칭성 이용해서 제 1사분면만 구하기
    for x in range(0, r2 + 1):
        y_max = isqrt(r2 * r2 - x * x)  # isqrt 정수 제곱근
        y_min = 0 if x >= r1 else ceil(sqrt(r1 * r1 - x * x))  # 제곱근 올
        answer += y_max - y_min + 1

    # 중복으로 더해진 축 위의 점들 빼주기
    answer = answer * 4 - (r2 - r1 + 1) * 4

    return answer