from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    # 단품메뉴 조합해서 코스로 재구성
    # 가장 많이 함께 주문한 단품메뉴들로 구성
    # 코스는 최소 2가지 이상, 최소 2명 이상의 손님으로부터
    answer = []

    for cnt in course:
        dict = defaultdict(int)
        for order in orders:
            order = sorted(order)  # "WXA"와 같은 경우 대비
            for i in combinations(order, cnt):
                dict[i] += 1

        if not dict or max(dict.values()) == 1:  # 최소 2명 이상의 손님
            continue

        max_value = max(dict.values())
        ans = ["".join(key) for key, value in dict.items() if value == max_value]
        answer.extend(ans)

    return sorted(answer)


"""
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]
"""

tcs = [
    [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]],
    [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],	[2,3,5]],
    [["XYZ", "XWY", "WXA"], [2,3,4]]
]

for tc in tcs:
    print(solution(*tc))
    print()