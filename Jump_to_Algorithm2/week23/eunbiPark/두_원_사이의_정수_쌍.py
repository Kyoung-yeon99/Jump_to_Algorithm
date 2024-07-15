import math


def solution(r1, r2):
    ans = 0

    for i in range(1, r2 + 1):
        # i 보다 r1이 작아 mn의 값이 음수가 되는 것 방지
        if i <= r1:
            mn = math.sqrt(math.pow(r1, 2) - math.pow(i, 2))
        else:
            mn = 0

        mx = math.sqrt(math.pow(r2, 2) - math.pow(i, 2))

        ans += (math.floor(mx) - math.ceil(mn) + 1)

    ans *= 4

    return ans
