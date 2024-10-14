# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack = []
    for n in number:
        # 스택이 비어있지 않고 제거할 숫자가 남았을 때 마지막 숫자가 더 크다면 하나 삭제 후 추가
        while stack and stack[-1] < n and k > 0: 
            stack.pop()
            k -= 1
        stack.append(n)

    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)