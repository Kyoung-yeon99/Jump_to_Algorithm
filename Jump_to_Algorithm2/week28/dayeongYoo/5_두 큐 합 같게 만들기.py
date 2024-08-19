from collections import deque


def solution(queue1, queue2):
    # 1. 두 큐에 담긴 원소 합/2 -> 각 큐의 합으로 만들어야 하는 수
    s_q1 = sum(queue1)
    s_q2 = sum(queue2)

    sum_q = (s_q1 + s_q2) // 2

    # 2. 덱으로 변경(popleft 연산 사용)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    # 총 연산 횟수
    move = 0

    # 두 큐를 번갈아 가면서 비교
    while s_q1 != sum_q:
        if s_q1 > sum_q:
            # 큐1 -> 큐2로 이동
            item = queue1.popleft()
            s_q1 -= item
            queue2.append(item)
        else:
            # 큐2 -> 큐1로 이동
            item = queue2.popleft()
            s_q1 += item
            queue1.append(item)
        move += 1

        if move > (len(queue1) + len(queue2)) * 2:
            return -1

    return move
