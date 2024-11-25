# 삼각형과 세변
while (True):
    triangle = list(map(int, input().split()))
    triangle.sort(reverse=True)
    a=triangle[0]
    b=triangle[1]
    c=triangle[2]
    if a==0 and b==0 and c==0:
        break
    elif a >= (b+c):
        print('Invalid')
    elif a==b==c:
        print('Equilateral')
    elif (a==b and b!=c) or (c==b and a!=c) or (c==a and b!=c):
        print('Isosceles')
    elif (a!=b and b!=c and c!=a):
        print('Scalene')
