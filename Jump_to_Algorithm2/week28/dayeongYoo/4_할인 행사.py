from collections import defaultdict


def solution(want, number, discount):
    answer = 0  # 회원등록 날짜 총 일수

    # 정현이가 원하는 제품: want
    # 원하는 제품의 수량: number
    # 키, 값으로 관리하기 위해 딕셔너리화
    want_dic = {}

    for i in range(len(want)):
        want_dic[want[i]] = number[i]

    while len(discount) >= 10:
        dc_dic = defaultdict(int)  # 할인 제품 딕셔너리
        # 10개씩 자르면서 할인제품의 제품, 수량이 원하는 제품, 수량이 맞는지 체크
        for j in range(10):
            dc_dic[discount[j]] += 1
        if all(dc_dic[w] == want_dic[w] for w in want_dic):
            answer += 1
        discount.pop(0)

    return answer
