def solution(t, p):
    ans = 0
    n = len(p)

    for p1 in range(len(t) - n + 1):
        if int(t[p1:p1 + n]) <= int(p):
            ans += 1

    return ans
