def solution(n, m, section):
    answer = 0

    if m == 1:
        return len(section)

    ss = 0
    for s in section:
        if ss == 0:
            answer += 1
            ss = s
        if s < ss + m:
            continue
        else:
            ss = s
            answer += 1

    return answer
