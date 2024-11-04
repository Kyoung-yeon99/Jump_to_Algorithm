from collections import defaultdict
# 조합 -> 시간초과


def solution(clothes):
    d = defaultdict(int)

    for name, category in clothes:
        d[category] += 1

    category_num = len(d.keys())
    values = list(d.values())
    if category_num == 1:
        answer = sum(values)
    else:
        answer = 1
        # A의 종류가 N개, B의 종류가 M개 일 때 선택하는 모든 경우의 수는 (N + 1)(M + 1) +1은 선택하지 않음을 의미
        # 모든 종류를 전부 선택하지 않았을 경우 제외하기 위해 -1 빼기
        for i in values:
            answer *= (i + 1)
        answer -= 1

    return answer