#  당구공을 시작 위치에서 목표 위치까지 당구공이 움직이는 최소 거리 구하기
#  당구공은 반드시 당구대 한 면을 '원쿠션' 해야 하며, '원쿠션' 전에 당구공이 목표 위치에 도달한다면 이는 올바른 루트가 아님

def solution(m, n, startX, startY, balls):
    def calculate_min_distance(ballX, ballY):
        # 공이 시작점과 같은 x 좌표에 있는 경우
        if ballX == startX:
            if ballY > startY:  # 공이 시작점보다 위에 있는 경우
                return min((startY + ballY) ** 2, (ballY - startY) ** 2 + 4 * min(ballX, m - ballX) ** 2)
            else:  # 공이 시작점보다 아래에 있는 경우
                return min((2 * n - startY - ballY) ** 2, (ballY - startY) ** 2 + 4 * min(ballX, m - ballX) ** 2)
        # 공이 시작점과 같은 y 좌표에 있는 경우
        elif ballY == startY:
            if ballX > startX:  # 공이 시작점보다 오른쪽에 있는 경우
                return min((startX + ballX) ** 2, (ballX - startX) ** 2 + 4 * min(ballY, n - ballY) ** 2)
            else:  # 공이 시작점보다 왼쪽에 있는 경우
                return min((2 * m - startX - ballX) ** 2, (ballX - startX) ** 2 + 4 * min(ballY, n - ballY) ** 2)
        # 공이 시작점과 다른 x, y 좌표에 있는 경우
        else:
            return min(
                (ballX - startX) ** 2 + min(startY + ballY, 2 * n - startY - ballY) ** 2,
                (ballY - startY) ** 2 + min(startX + ballX, 2 * m - startX - ballX) ** 2
            )

    # 각 공에 대한 최소 거리를 계산하여 리스트로 반환
    return [calculate_min_distance(ball[0], ball[1]) for ball in balls]
