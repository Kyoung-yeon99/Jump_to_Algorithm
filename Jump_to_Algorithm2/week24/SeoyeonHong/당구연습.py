# https://school.programmers.co.kr/learn/courses/30/lessons/169198

# 각 회마다 공이 굴러간 거리의 최솟값의 제곱의 배열
def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        distance = [] # 공을 상하좌우 상하좌우에 원쿠션 했을 때 이동거리 제곱
        x, y = ball
        # 주의 - 쿠션에 맞기 전에 공이 맞는 경우 제외
        # 위쪽 벽에 맞힐 경우
        if not (x == startX and y > startY):
            distance.append((startX - x) ** 2 + (n * 2 - y - startY) ** 2)
        # 아래쪽 벽에 맞힐 경우
        if not (x == startX and y < startY):
            distance.append((startX - x) ** 2 + (y + startY) ** 2)
        # 왼쪽 벽에 맞힐 경우
        if not (y == startY and x < startX):
            distance.append((x + startX) ** 2 + (y - startY) ** 2)
        # 오른쪽 벽에 맞힐 경우
        if not (y == startY and x > startX):
            distance.append((2 * m - x - startX) ** 2 + (y - startY) ** 2) 

        answer.append(min(distance))

    return answer

print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))