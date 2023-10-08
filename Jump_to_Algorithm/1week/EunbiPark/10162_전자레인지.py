# A: 300초, B: 60초, C: 10초
# 버튼을 적절히 눌러 합이 정확히 T 초가 되도록
# 버튼을 누른 횟수는 항상 최소가 되도록 (최소버튼 조작)
# 만들 수 없다면 -1 출력

t = int(input())

a, b, c = 0, 0, 0

a = t // 300
a_temp = t % 300
b = a_temp // 60
b_temp = a_temp % 60
c = b_temp // 10


if b_temp % 10 > 0:
    print(-1)
else:
    print(a, b, c)

