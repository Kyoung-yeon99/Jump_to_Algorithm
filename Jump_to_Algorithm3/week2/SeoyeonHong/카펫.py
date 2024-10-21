import math

def solution(brown, yellow):
    total = brown + yellow # 전체 격자 수
    for r in range(1, int((math.sqrt(total)))+1): # 가로 >= 세로
        if total % r == 0: # r이 가능한 세로 길이(정수)
            c = total // r 
            if (r + c) == (brown//2 + 2): 
                return [c, r]

# 가로:c, 세로:r, b: 갈색 격자 수, y: 노란색 격자 수
# r * c = y + b
# (r-2) * (c-2) = y
# r * c - 2 * (r+c) + 4 = y
# y + b - 2 * (r+c) + 4 = y
# r + c = b / 2 + 2
         