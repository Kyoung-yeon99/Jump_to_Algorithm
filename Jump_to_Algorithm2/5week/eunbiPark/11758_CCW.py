# ccw 알고리즘 활용 - 기하 알고리즘의 기초
# 평면에 놓여진 세 점의 방향 관계를 구하는 알고리즘
# 신발끈 공식 활용

dots = []
for _ in range(3):
    dots.append(list(map(int, input().split())))

def ccw(p1, p2, p3):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])

ret = ccw(dots[0], dots[1], dots[2])

if ret > 0:
    print(1)
elif ret == 0:
    print(0)
else:
    print(-1)