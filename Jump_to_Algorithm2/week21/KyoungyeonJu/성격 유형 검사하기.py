from collections import defaultdict


def solution(survey, choices):
    d = defaultdict(int)

    # 각 성격 유형의 점수 Update
    for s, c in zip(survey, choices):
        da = s[0]  # 비동의 성격 유형
        a = s[1]  # 동의 성격 유형

        if c == 4:
            continue
        elif c < 4:
            d[da] += (4 - c)
        elif c > 4:
            d[a] += (c - 4)

    answer = ''
    characters = ['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']
    for c1, c2 in characters:
        if d[c1] < d[c2]:
            answer += c2
        else:
            answer += c1

    return answer


"""
d가 defaultdict이므로 값이 없는 경우에도 계산 가능
아래 코드는 처음 생각했던 코드 - 4가지 경우의 수로 나누어서 계산 

        if (c1 not in d) and (c2 not in d):  # 두 유형 모두 값이 없는 경우
            answer += c1
        else:  # 값이 하나라도 있는 경우
            if d[c1] > d[c2]:
                answer += c1
            elif d[c1] < d[c2]:
                answer += c2
            else:
                answer += c1
"""