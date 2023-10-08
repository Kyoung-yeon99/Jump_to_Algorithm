# 음식 평론가
# 최대공약수 구하는 함수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 소시지 수 n 평론가 수 m
n, m = map(int, input().split())
result = m - gcd(n, m)
# n과 m의 최대공약수가 m이면, 즉 n%m==0이면 result는 0
# n과 m의 최대공약수가 1이면, result = m-1
print(result)
