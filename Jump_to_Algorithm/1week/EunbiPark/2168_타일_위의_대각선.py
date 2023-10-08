# 접근 못함 -> 유클리드 호제법

# 대각선이 꼭지점을 지나가지 않는다면 x + y - 1
# 대각선이 꼭지점을 지나간다면 x + y - 1 - (꼭지점 개수)
    # 꼭지점의 개수: x , y의 최대 공약수 -1

# => x + y - gcd(x, y)

x, y = map(int, input().split())

def gcd(x, y):
    if y > x:
        x, y = y, x

    # 유클리드 호제법을 사용하여 gcd 구하기
    while 1:
        if y == 0:
            break
        x, y = y, x % y
    return x

print(x + y - gcd(x, y))

'''
# 시간 초과 
def gcd(x, y):
    minimum = min(x, y)
    for i in range(minimum, 0, -1):
        print(i)
        if x % i == 0 and y % i == 0:
            return i
    else: 0

'''
