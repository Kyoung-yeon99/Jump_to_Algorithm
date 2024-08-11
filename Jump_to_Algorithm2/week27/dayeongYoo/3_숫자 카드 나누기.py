import math
from functools import reduce  # functools 모듈에서 reduce 함수만 사용하겠음


def solution(arrayA, arrayB):
    answer = 0

    # 주어진 배열의 최대공약수 구하는 함수
    def get_gcd(arr):
        return reduce(math.gcd, arr)

    # arrA, arrB 각각 최대 공약수 구하기
    gcd_a = get_gcd(arrayA)
    gcd_b = get_gcd(arrayB)

    # gcd가 다른 배열의 모든 원소를 나눌 수 없는지 체크
    def is_div(gcd, arr):
        for num in arr:
            if num % gcd == 0:
                return False
        return True

    # 조건에 맞는지 확인 후 결과 반환
    if is_div(gcd_a, arrayB):
        answer = gcd_a
    if is_div(gcd_b, arrayA):
        answer = max(answer, gcd_b)

    return answer
