tra = [int(input()) for _ in range(3)]

if sum(tra) == 180:  # 1번째 분기
    if tra.count(60) == 3:  # 모든 각이 60도
        print("Equilateral")
    elif tra[0] == tra[1] or tra[1] == tra[2] or tra[0] == tra[2]:
        print("Isosceles")
    else:
        print("Scalene")

else:
    print("Error")
