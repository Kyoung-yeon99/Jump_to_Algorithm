def solution(order):  # order: 원하는 순서
    # 실을 수 있는 상자 개수
    answer = 0

    # 기존 택배 순서
    n = len(order)

    # 보조 컨테이너
    sub_con = []

    # 인덱스
    idx = 0

    for box in range(1, n + 1):
        if box == order[idx]:  # 순서가 일치하면
            idx += 1
            answer += 1  # 트럭에 싣는 상자수 +1
        else:
            # 순서가 일치하지 않다면
            # 보조 컨테이너에 보관
            sub_con.append(box)

        while sub_con and sub_con[-1] == order[idx]:
            # 보조컨테이너에서 뺀 값이 원하는 순서와 일치한다면
            sub_con.pop()
            answer += 1
            idx += 1

    return answer
