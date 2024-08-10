import math
def solution(arrayA, arrayB):
    # 공약수
    ans = 0
    a_gcd = arrayA[0]
    b_gcd = arrayB[0]
    
    for x, y in zip(arrayA, arrayB):
        a_gcd = math.gcd(a_gcd, x)
        b_gcd = math.gcd(b_gcd, y)
    
    a_flag, b_flag = True, True # 나누어지지 않으면 true - 만족하는 카드가 있음 
    for x, y in zip(arrayA, arrayB):
        if x % b_gcd == 0:
            a_flag = False 
        if y % a_gcd == 0:
            b_flag = False 
    
    if not a_flag and not b_flag:
        return 0
    else:
        return max(a_gcd, b_gcd)
