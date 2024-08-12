from itertools import product


def solution(users, emoticons):
    # 이모티콘 할인 행사의 목표 1이 우선
    # 1. 플러스 가입자 최대한 늘리기
    # 2. 판매액 최대한 늘리기

    # 기준에 따라 일정 비율 이상 할인하는 이모티콘 모두 구매
    # 이모티콘 구매 비용의 합이 일정 가격 이상이면, 플러스 가입

    pers = [0.9, 0.8, 0.7, 0.6]
    answer = []

    for row in product(pers, repeat=len(emoticons)):
        row = list(zip(emoticons, list(row)))
        plus, total_pay = 0, 0

        for u in users:
            ratio = (100 - u[0])/100
            rr = filter(lambda x: x[1] <= ratio, row)
            pay = 0
            for r in rr:
                pay += r[0]*r[1]

            if pay >= u[1]:
                plus += 1
                pay = 0

            total_pay += pay

        if plus == 0 and total_pay == 0:
            continue
        answer.append([plus, total_pay])

    answer = sorted(answer, key=lambda x: (-x[0], -x[1]))

    return [answer[0][0], int(answer[0][1])]