from collections import deque


def solution(numbers):
    answer = [-1]  # 맨 마지막 값은 뒤에 값이 없기 때문에 무조건 -1
    s = deque()  # 스택
    s.append(numbers[-1])  # 맨 마지막 값 append

    for i in range(len(numbers) - 2, -1, -1):  # 뒤에서 두번째 값부터 시작
        while len(s) != 0:  # 스택에 값이 있는 있을 경우에만, pop한 값이 현재 값보다 크면 break, 아니면 계속 pop
            top = s.pop()
            if top > numbers[i]:
                break

        if top <= numbers[i]:  # top 값이 현재 값과 같거나 작으면 answer에 -1
            answer.append(-1)
        else:
            answer.append(top)  # top 값이 현재 값보다 크면, answer에 top
            s.append(top)  # 스택에 다시 append

        s.append(numbers[i])  # 현재 값도 스택에 append

    answer = answer[::-1]  # 뒤에서부터 탐색했기 때문에 역순

    return answer