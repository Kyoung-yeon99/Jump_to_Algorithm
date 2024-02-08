# 삼각형의 세 각
a1 = int(input())
a2 = int(input())
a3 = int(input())

if a1 + a2 + a3 != 180: # 세 각의 합이 180이 아닌 경우
    print('Error')
else:
    if a1 == a2 == a3: # 세 각의 크기가 모두 60일 경우
        print('Equilateral')
    elif a1 == a2 or a2 == a3 or a3 == a1: # 두 각이 같은 경우
        print('Isosceles')
    else: # 같은 각이 없는 경우
        print('Scalene')