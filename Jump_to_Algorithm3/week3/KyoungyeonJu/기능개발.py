from math import ceil


def solution(progresses, speeds):
    days, answer = [], []
    for p, s in zip(progresses, speeds):
        days.append(ceil((100 - p) / s))

    print(days)
    d, cnt = days[0], 1
    for i in days[1:]:
        if d < i:
            answer.append(cnt)
            d, cnt = i, 1
        else:
            cnt += 1

    answer.append(cnt)
    return answer