while True:
    l = list(map(int, input().split()))
    if sum(l) == 0:
        break
    s = set(l)
    if len(s) == 1: # 세 변의 길이가 같을 경우
        print("Equilateral")
    elif max(l) * 2 < sum(l): # 삼각형의 조건을 만족한다면
        if len(s) == 2: # 두 변의 길이가 같을 경우
            print("Isosceles")
        else: # 세 변의 길이가 모두 다를 경우
            print("Scalene")
    else:
         print("Invalid")

