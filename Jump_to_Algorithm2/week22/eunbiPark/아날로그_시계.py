def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    # 초단위로 변경
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    # 포함되지 않는 시작 시간 00, 12 미리 카운팅
    if start == 0 * 3600 or start == 12 * 3600:
        answer += 1

    # 1초씩 이동 (start: 현재 시간)
    while start < end:
        # 현재 시간의 각 침의 위치 구하기
        h_angle = start / 120 % 360  # 1시간에 30도 (1초에 30/3600)
        m_angle = start / 10 % 360  # 1초에 6/60도
        s_angle = start * 6 % 360  # 1초에 6도

        # 1초를 움직였을 때의 위치
        # 360도가 아닌 0도가 되어 카운팅 안되는 것 방지 -> 1초 더 이동시켰을 때 360가 되는지
        # 이동했을 때 지나쳤는지, 같아졌는지를 비교
        h_next = 360 if (start + 1) / 120 % 360 == 0 else (start + 1) / 120 % 360
        m_next = 360 if (start + 1) / 10 % 360 == 0 else (start + 1) / 10 % 360
        s_next = 360 if (start + 1) * 6 % 360 == 0 else (start + 1) * 6 % 360

        # 일반적인 경우
        # 초침이 시/분침 전 -> 1초 후 시/분침과 같은 위치 혹은 넘어선 위치
        if s_angle < h_angle and s_next >= h_next:
            answer += 1
        if s_angle < m_angle and s_next >= m_next:
            answer += 1

        # 시/분침이 동시에 겹쳤을 경우
        if s_next == h_next and h_next == m_next:
            answer -= 1

        start += 1

    return answer