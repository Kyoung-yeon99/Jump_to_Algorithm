def solution(friends, gifts):
    answer = 0

    f = {name: idx for idx, name in enumerate(friends)}
    l = len(friends)

    m = [[0] * l for _ in range(l)]

    for g in gifts:
        a, b = g.split(" ")
        giver = f[a]
        taker = f[b]
        m[giver][taker] += 1

    for i in range(l):
        for j in range(i + 1, l):
            if m[i][j] > m[j][i]:
            elif m[i][j] < m[j][i]:
            else:

    return answer