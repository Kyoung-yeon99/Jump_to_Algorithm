def solution(k, ranges):
    x = 0
    area, answer = [], []

    while k > 1:
        if k % 2 == 0:
            nk = k // 2
        else:
            nk = k * 3 + 1
        area.append((k + nk) / 2)
        k = nk
        x += 1

    for s, e in ranges:
        if e <= 0:
            e = x + e

        if s > e:
            answer.append(-1)
        else:
            answer.append(sum(area[s:e]))

    return answer
