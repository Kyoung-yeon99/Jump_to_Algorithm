def solution(friends, gifts):
    # 1. 이름 idx 처리 
    idx = {}
    for i, f in enumerate(friends):
        idx[f] = i

    # 2. 선물 테이블 생성 (행: 준 사람, 열: 받은 사람, gift[준사람][-1] : 선물 지수)
    tbl = [[0 for _ in range(len(friends) + 1)] for _ in range(len(friends))]

    # 3. 주고 받은 선물 표시
    for gift in gifts:
        a, b = gift.split()
        tbl[idx[a]][idx[b]] += 1

    # 4. 선물 지수 계산 
    # 4-1. 받은 선물 계산 
    for j in range(len(friends)):
        temp = 0
        for i in range(len(friends)):
            temp += tbl[i][j]
        tbl[j][-1] = temp

    # 4-2. 선물 지수 계산 (준선물 - 받은 선물)
    for i in range(len(friends)):
        temp = sum(tbl[i][:-1])
        tbl[i][-1] = temp - tbl[i][-1]

    # 5. 조건 판단
    next = [0 for _ in range(len(friends))]  # 받을 선물의 수 기록

    # 5-1. 주고 받은 선물이 있다면 
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if tbl[i][j] or tbl[j][i]:  # 주고 받은 선물이 있다면
                if tbl[i][j] > tbl[j][i]:  # i가 더 많이 줌
                    next[i] += 1
                elif tbl[i][j] < tbl[j][i]:  # j가 더 많이 줌
                    next[j] += 1

                else:  # 주고 받은 수가 같음 -> 선물 지수 비교
                    if tbl[i][-1] > tbl[j][-1]:
                        next[i] += 1
                    elif tbl[i][-1] < tbl[j][-1]:
                        next[j] += 1

            else:  # 주고 받은 선물이 없다면
                if tbl[i][-1] > tbl[j][-1]:
                    next[i] += 1
                elif tbl[i][-1] < tbl[j][-1]:
                    next[j] += 1

    # debug
    for b in tbl:
        print(*b)
    print()
    print(*next)

    return max(next)