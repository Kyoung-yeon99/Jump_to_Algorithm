# 0층으로 가기 위해 필요한 돌의 최솟값?
# 버튼 1번 = 돌 1개 소요

def solution(storey):  # 현재 층
    # 버틑 클릭수
    answer = 0

    # 0층이 될때까지
    while storey > 0:
        # 현재 층의 마지막 자릿수 저장
        digit = storey % 10

        if digit > 5:
            # 현재 자리의 숫자가 5보다 크다면 올림
            answer += 10 - digit  # 지금 숫자에서 더할 1의 자리
            storey = storey // 10 + 1  # 10의 자리 올림
        elif digit < 5:
            # 현재 자리의 숫자가 5보다 작다면 내려서 0으로 만듦
            answer += digit
            storey //= 10  # 1의 자리 뺀 수 -> 몫만 취함
        else:
            # 현재 자리의 숫자가 5일 경우
            # 다음 자리수가 5 이상이면 올리고, 아님 내림
            next_digit = (storey // 10) % 10
            if next_digit >= 5:
                answer += 10 - digit
                storey = storey // 10 + 1
            else:
                answer += digit
                storey //= 10

    return answer
