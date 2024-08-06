# 우선순위
# 1.이모티콘 플러스 서비스 가입자 수 늘리기
# 2.이모티콘 판매액 최대로 늘리기

# 1. 가능한 할인율 조합
# 10, 20, 30, 40% 중 하나의 할인율 적용(4^m 가지)

# 2. 각 조합에 대한 서비스 가입자 수/ 판매액 계산
# 할인율 조합에 대해 이모티콘 구매 or 서비스 가입할지 계산

# 3. 최적 결과 선택
# 가입자 수가 동일한 경우, 판매액이 가장 큰 조합 선택
from itertools import product


def solution(users, emoticons):
    # 할인율
    dc_rate = [10, 20, 30, 40]
    # 가입자수
    max_sub = 0
    # 판매액
    max_buy = 0

    # 모든 할인율 조합 계산
    for dc in product(dc_rate, repeat=len(emoticons)):
        sub = 0
        buy = 0
        for user in users:
            user_rate, user_price = user
            total = 0
            # 각 사용자가 구매할 이모티콘 총액 계산
            for i in range(len(emoticons)):
                if dc[i] >= user_rate:
                    total += emoticons[i] * (100 - dc[i]) // 100
            # 총액이 기준 가격을 넘으면 이모티콘 플러스 가입
            if total >= user_price:
                sub += 1
            else:
                buy += total
        # 최대 가입자 수와 판매액 업데이트
        if sub > max_sub:
            max_sub = sub
            max_buy = buy
        elif sub == max_sub:  # 같을때는 가격으로 비교
            max_buy = max(max_buy, buy)
    return [max_sub, max_buy]
