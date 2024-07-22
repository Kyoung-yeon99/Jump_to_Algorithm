from collections import deque


def solution(cards1, cards2, goal):
    for word in goal:
        if len(cards1) != 0 and cards1[0] == word:
            cards1.pop(0)
        elif len(cards2) != 0 and cards2[0] == word:
            cards2.pop(0)
        else:
            return 'No'
            break

    return 'Yes'


"""
# deque 사용 

    q1 = deque(cards1)
    q2 = deque(cards2)

    for word in goal:
        if len(q1) != 0 and q1[0] == word:
            q1.popleft()
            continue
        elif len(q2) != 0 and q2[0] == word:
            q2.popleft()
            continue
        else:
            return 'No'
            break

    return 'Yes'
"""