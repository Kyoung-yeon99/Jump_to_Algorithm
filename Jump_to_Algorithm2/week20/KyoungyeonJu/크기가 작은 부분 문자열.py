def solution(t, p):
    answer = 0
    tl = len(t)
    pl = len(p)
    pp = int(p)

    for i in range(tl - pl + 1):
        num = int(t[i:i + pl])
        if num <= pp:
            answer += 1

    return answer