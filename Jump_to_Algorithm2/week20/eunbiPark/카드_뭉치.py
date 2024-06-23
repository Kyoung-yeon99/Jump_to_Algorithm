def solution(cards1, cards2, goal):
    p1, p2, cnt = 0, 0, 0

    while cnt < len(goal):
        if len(cards1) > p1 and cards1[p1] == goal[cnt]:
            cnt += 1
            p1 += 1

        elif len(cards2) > p2 and cards2[p2] == goal[cnt]:
            cnt += 1
            p2 += 1

        else:
            return "No"

    return "Yes"