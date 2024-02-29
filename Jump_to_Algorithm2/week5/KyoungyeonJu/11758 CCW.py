x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
# 외적구하기 (x1y2+x2y3+x3y1) - (x2y1+x3y2+x1y3)
cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)

if cross_product > 0:
    print(1)  # 반시계 방향
elif cross_product < 0:
    print(-1)   # 시계 방향
else:
    print(0)   # 일직선
