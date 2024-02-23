# 2차원 좌표 평면 위 점 3개(p1, p2, p3)
# p1, p2, p3를 이은 선분이 어떤 방향?

# 예제 1이 이해가 안가는데..?
# 3개를 이으면 밑변이 없는 삼각형 모양인데, 이게 무슨 방향,,,?

# ccw : counter clockwise(세점의 방향성 판별 알고리즘)
# a,b,c 세 점을 순서대로 이었을 때 시계방향이면 음수 출력. 반시계방향이면 양수 출력. 일직선이면 0 출력

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# 외적값
cp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

if cp < 0:
    print(-1)
elif cp > 0:
    print(1)
else:
    print(0)
