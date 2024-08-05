# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product

def solution(users, emoticons):
    rate = [10, 20, 30, 40]
    discounts = list(product(rate, repeat=len(emoticons)))
    max_user = 0
    max_purchase = 0
    for i in range(len(discounts)): # 각 할인률 조합에 대해
        service_user = 0 # 서비스 가입한 사용자 수
        total_purchase = 0 # 총 판매액

        for j in range(len(users)): # 각 사용자에 대해
            purchase = 0 # 총 구매액

            for k in range(len(emoticons)): # 각 아이템에 대해
                if discounts[i][k] >= users[j][0]: # 일정 비율 이상 할인한다면 구매
                    purchase += emoticons[k] * (100 - discounts[i][k]) // 100

            if purchase >= users[j][1]: # 구매 비용의 합이 일정 가격 이상일 경우 서비스 가입
                service_user += 1
            else: # 서비스에 가입하지 않았을 경우 판매액 합산
                total_purchase += purchase

        if service_user > max_user:
            max_user = service_user
            max_purchase = total_purchase
        elif service_user == max_user:
            max_purchase = max(max_purchase, total_purchase)

    return ([max_user, max_purchase]) # 이모티콘 플러스 서비스 가입 수, 이모티콘 매출액
            

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))