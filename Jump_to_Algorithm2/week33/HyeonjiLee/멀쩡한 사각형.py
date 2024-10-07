import math

def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))

# def solution(w, h):
#     answer = 0
#
#     for i in range(1, w):
#         n = (h * i) / w
#         answer += int(n)
#
#     answer *= 2
#     return answer

print(solution(8,12))