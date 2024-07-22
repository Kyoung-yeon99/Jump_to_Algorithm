def solution(friends, gifts):
    f = {name: idx for idx, name in enumerate(friends)}  # 이름과 인덱스 매칭 딕셔너리
    l = len(friends)
    g = [0] * l  # 다음 달에 받을 선물 리스트
    m = [[0] * l for _ in range(l)]  # 이번 달에 받은 선물 인접 행렬

    # 받은 선물 2차원 리스트 m Update
    for gift in gifts:
        a, b = gift.split(" ")
        giver = f[a]
        taker = f[b]
        m[giver][taker] += 1

    # 서로 받은 선물 비교해서 다음 달에 받을 선물 리스트 g Update
    for i in range(l):
        for j in range(i + 1, l):
            if m[i][j] > m[j][i]:
                g[i] += 1
            elif m[i][j] < m[j][i]:
                g[j] += 1
            else:
                nm = list(map(list, zip(*m)))  # 2차원 리스트 전치 transpose

                i_idx = sum(m[i]) - sum(nm[i])
                j_idx = sum(m[j]) - sum(nm[j])

                if i_idx > j_idx:
                    g[i] += 1
                elif i_idx < j_idx:
                    g[j] += 1

    return max(g)