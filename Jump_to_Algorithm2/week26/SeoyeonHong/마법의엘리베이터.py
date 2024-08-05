# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0

    while storey:
        remainder = storey % 10

        if remainder > 5: # 6 ~ 9
            answer += (10 - remainder)
            storey += 10
        elif remainder < 5: # 0 ~ 4
            answer += remainder
        else: # 5
            if (storey // 10) % 10 > 4: # 다음 자릿값이 크면 10으로, 작으면 0으로
                storey += 10
            answer += remainder
        storey //= 10

    return answer
