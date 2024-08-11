# 롤케이크 2조각으로 자르기
# 각 조각에 "동일한 가짓수의 토핑"이 올라가면 공평하게 롤케이크 나눠진 거임
# 4가지 종류 토핑
# [1,2,1,3,1,4,1,2] 순서로 올려짐
# 만약 [1,2,1/ 3,1,4,1,2] 로 자르면
# a: [1,2,1]/ b: [3,1,4,1,2]
# a: 2가지 토핑/b: 4가지 토핑 -> "불공평"

# 1) [1,2,1,3/ 1,4,1,2] 로 자르면
# a,b 둘다 3가지 토핑 -> "공평"
# 2) [1,2,1,3,1/ 4,1,2]
# a,b 둘다 3가지 토핑 -> "공평"
# 공평하게 자르는 방법의 수?

from collections import defaultdict  # 키가 존재하지 않을때, 자동으로 기본값 생성해줌(기본값: 생성시 사용한 안자)


def solution(topping):
    answer = 0
    # 1차 시도: 순서대로 2등분 해가면서 해당 리스트에서 key 개수가 동일하면 answer +1 -> 시간초과
    # 2차 시도: 전체 토핑 종류 카운트 -> 오른쪽, 왼쪽 토핑 종류 카운트 유지해가면서 이동
    n = len(topping)

    # 전체 토핑 개수 세기
    top_count = defaultdict(int)
    for top in topping:
        top_count[top] += 1
    # 왼쪽, 오른쪽 나눈 조각의 토핑 카운트
    left_cake = defaultdict(int)
    right_cake = top_count.copy()  # 딕셔너리 원본데이터 변경 방지 -> 복사본

    # 왼쪽 토핑 종류 세기용
    left_type = set()

    for i in range(n - 1):
        cur_top = topping[i]

        # 왼쪽 조각 업데이트
        if left_cake[cur_top] == 0:
            left_type.add(cur_top)
        left_cake[cur_top] += 1

        # 오른쪽 조각 업데이트
        right_cake[cur_top] -= 1
        if right_cake[cur_top] == 0:  # 오른쪽 조각에서 해당 토핑 삭제
            del right_cake[cur_top]

        # 왼쪽, 오른쪽 조각의 토핑 종류가 동일하다면
        if len(left_cake) == len(right_cake):
            answer += 1

    return answer