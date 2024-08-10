# 반지름이 d인 원 내부에 존재
def solution(k, d):
    ans = 0
    mul = 0
    while mul <= d:
        line = (d ** 2 - mul ** 2) ** 0.5
        ans += int(line) // k + 1
        mul += k
    
    return ans
