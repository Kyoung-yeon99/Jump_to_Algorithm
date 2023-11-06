import math
n = int(input())
count = 0

def numOfComb(n, r): # 조합 개수 구하는 함수
    c = 1
    if n > r:
        for i in range(n, n-r, -1):
            c *= i
        c //= math.factorial(r)
    return c

for i in range(1, 11): # i개의 숫자로 이루어진 수
    if n >= i :
        count += numOfComb(n-1, i-1) * numOfComb(10, i) # 숫자가 바뀌는 자리 * i개 숫자 조합 

print(count % 10007)
