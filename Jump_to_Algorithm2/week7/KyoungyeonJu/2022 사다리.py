from math import sqrt


def get_c(mid):
    a = sqrt(x**2-mid**2)
    b = sqrt(y**2-mid**2)
    return a*b/(a+b)


x, y, c = map(float, input().split())  # int 아니고 float!!!
start, end = 0, min(x, y)  # x와 y 중 작은 값이 end
result = 0
# 오차 10-3까지 허용인데 get_c 함수에서 제곱하기 때문에 1e-6보다 클 때까지 반복
while end-start > 1e-6:
    mid = (start+end)/2  # 이분탐색
    if get_c(mid) >= c:
        result = mid
        start = mid
        # print(f"mid={mid} get_c(mid)={get_c(mid)}")
    else:
        end = mid
        # print("else end=", mid)

print("%0.3f"%result)  # 오차는 10-3까지 허용하므로 소수점 3자리까지 출력


"""
from sympy import symbols, solve

x, y, c = map(int, input().split())
a, a1 = symbols("a, a1")  # a1+a2=a, a2 = a-a1
answer = list(solve([
    c*a - a1*((y**2 - a**2)**(1/2)),
    c*a - (a-a1)*((x**2 - a**2)**(1/2)),
    a1*((x**2 - a**2)**(1/2)) - a*((x**2 - a**2)**(1/2)) + c*a,
    (a-a1)*((y**2 - a**2)**(1/2)) - a*((y**2 - a**2)**(1/2)) + c*a
]))

print("%0.3f" %answer[0])
"""