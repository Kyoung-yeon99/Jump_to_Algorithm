angle = []
for _ in range(3):
    angle.append(int(input()))

if sum(angle) != 180:  # 삼각형이 아닌 경우
    print("Error")
elif len(set(angle)) == 1:  # 정삼각형
    print("Equilateral")
elif len(set(angle)) == 2:  # 이등변 삼각형
    print("Isosceles")
else:  # 그 이외의 삼각형
    print("Scalene")
