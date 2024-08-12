import math


def solution(k, d):
    answer = 0
    for i in range(d//k+1):
        x = k*i
        y = math.isqrt(d*d - x*x)  # 정수 제곱근
        # print(f"x= {x}, y = {math.isqrt(d*d - x*x)}")
        if y == 0:
            answer += 1
        else:
            answer += (y//k+1)

    return answer