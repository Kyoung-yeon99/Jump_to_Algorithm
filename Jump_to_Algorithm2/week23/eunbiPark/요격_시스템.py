def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))

    idx, cnt = 0, 1
    for i in range(1, len(targets)):
        if targets[idx][1] <= targets[i][0]:
            cnt += 1
            idx = i

    return cnt