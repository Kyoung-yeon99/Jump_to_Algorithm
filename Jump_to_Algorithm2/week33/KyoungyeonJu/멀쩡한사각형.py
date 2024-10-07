def solution(w,h):
    # 1억 100,000,000
    # 전체 w*h
    # 멀쩡한 사각형 (w-1)*(h-1)
    # 안 멀쩡한 사각형 w+h-1 = wh - (wh-w-h+1)
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    gcd_num = gcd(w, h)
    nw, nh = w//gcd_num, h//gcd_num
    answer = w*h - (nw+nh-1)*gcd_num

    return answer