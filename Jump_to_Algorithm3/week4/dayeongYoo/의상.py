def solution(clothes):
    answer = 1
    # 최소 1개의 이상 착용해야 함 -> 의상 착용 O,X 2가지 경우임. 따라서 선택지는 해당 의상개수 +1(=안 입는 경우)
    # 각 종류별 최대 1가지 의상 착용 가능

    # 딕셔너리 key-value로 저장
    dic = {}

    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = 1
        else:
            dic[cloth[1]] += 1
            # 조합 계산
    for com in dic.values():
        answer *= (com + 1)

    return answer - 1  # 의상을 아무것도 안 입는 경우 제외
