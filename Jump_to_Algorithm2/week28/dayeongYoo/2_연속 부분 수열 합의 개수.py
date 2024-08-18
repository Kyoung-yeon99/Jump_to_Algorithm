def solution(elements):  # elements: 원형 수열의 모든 원소
    # 연속 부분 수열로 만들 수 있는 수 개수
    answer = 0

    # 수열 -> 원형 수열로 만들기
    circle_sy = elements + elements[:-1]

    # 원형 수열에서 연속 부분 수열 구하기
    n = 1  # 부분 수열 길이
    # 중복 제외 부분 수열의 합
    sum_sub_list = set()

    while n <= len(elements):
        for i in range(len(circle_sy) - n + 1):
            sub_list = circle_sy[i:i + n]
            sum_sub_list.add(sum(sub_list))  # 부분 수열의 합 저장
        n += 1  # 길이 증가

    # 중복 제외-> 집합화: set()
    answer = len(sum_sub_list)
    return answer
