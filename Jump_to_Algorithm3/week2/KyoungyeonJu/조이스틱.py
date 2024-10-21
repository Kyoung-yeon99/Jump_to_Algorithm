def solution(name):
    answer, l = 0, len(name)
    min_ = l - 1  # 최대값

    for i in range(l):
        alpha = name[i]
        answer += min(ord(alpha)-ord('A'), ord('Z')-ord(alpha)+1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < l and name[next] == 'A':
            next += 1

        min_ = min(min_, 2*i+l-next, i+2*(l-next))  # min_, 오->시->왼, 왼->시->오

    return answer+min_


"""
"JEROEN"	56
"JAN"	23
"""

tcs = [
    "JEROEN",
    "JAN"
]

for tc in tcs:
    print(solution(tc))
    print()