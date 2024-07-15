def solution(targets):
    answer, cur = 0, 0
    targets = sorted(targets, key=lambda x: x[1])

    for i in range(len(targets)):
        if cur > targets[i][0]:
            continue
        else:
            cur = targets[i][1]
            answer += 1

    return answer

