# 타일 위의 대각선
# 가로 x, 세로 y
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


x, y = map(int, input().split())
gcd_num = gcd(x, y)
width = x//gcd_num
height = y//gcd_num
result = gcd_num*(width+height-1)
print(result)

