import math
x, y = map(int, input().split())
print(x + y - math.gcd(x, y))

'''
x-1개의 세로줄, y-1개의 가로줄을 지남
최대공약수 만큼은 꼭짓점을 지남
대각선이 그어진 타일의 개수 = x + y - gcd(x, y)
'''

# 다른 풀이 - 시간 초과
'''
import math
x, y = map(int, input().split())
if x == y:
    print(x)
else:
    gcd = math.gcd(x, y)
    x //= gcd
    y //= gcd
    c = 0
    for a in range(x):
        c += math.ceil(y / x * (a + 1)) - math.floor(y / x * a)
    print(c * gcd)
'''