a = int(input())
b = int(input())
c = int(input())

total = a + b + c

if a == b == c == 60:
    print('Equilateral')
elif total == 180:
    if a == b != c or a != b == c or a == c != b:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')

'''
if sum(triangles) == 180:
    if triangles[0] == triangles[1] == triangles[2] == 60:
        print('Equilateral')
    elif triangles[0] == triangles[1]:
        print('Isosceles')
    elif triangles[0] == triangles[2]:
        print('Isosceles')
    elif triangles[1] == triangles[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
'''