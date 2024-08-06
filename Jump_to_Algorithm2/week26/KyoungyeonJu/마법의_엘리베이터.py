def solution(storey):
    # 그리디
    # 마법의 엘리베이터 절대값 10^c (c ≥ 0 인 정수) 형태 정수들이 적힌 버튼
    # 버튼 누르면, 현재 층 + 버튼 값 더한 층으로 이동, 결과값이 0보다 작으면 움직이지 않음
    # 0층이 가장 아래층, 엘리베이터는 현재 민수가 있는 층에 있음
    # 최소한의 버튼을 눌러 이동

    a, b = 10, 1
    answer = 0
    while storey > 0:
        # 일의 자리 수부터 각 자리의 값
        num = storey % (a ** b)
        num = num // (a ** (b - 1))

        if num < 5:  # 5보다 작은 경우
            answer += num
            storey -= num * (a ** (b - 1))
        elif num > 5:  # 5보다 큰 경우
            answer += (10 - num)
            storey += (10 - num) * (a ** (b - 1))
        elif num == 5:  # 5인 경우
            before_num = storey // (a ** b) % 10  # 앞자리 수의 값
            if before_num >= 5:
                answer += (10 - num)
                storey += (10 - num) * (a ** (b - 1))
            else:
                answer += num
                storey -= num * (a ** (b - 1))
        b += 1

    return answer


tcs = [
    (1000,  1),
    (56, 9),
    (46, 9),
    (155, 11),
    (55, 10),
    (75, 8),
    (555, 14),
    (123456789, 22)
    # (646, 13),
    # (555, 14),
    # (485, 11),
    # (95, 6),
    # (75, 8),
    # (5654, 17),
    # (5555, 18),
    # (65, 9),
    # (57595358, 26),
    # (16, 6),
    # (2554, 16)
]

for tc in tcs:
    print(solution(tc[0]), "기대값:", tc[1])
    print()
