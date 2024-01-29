from collections import deque
iron = input()
iron_s = deque()  # 스택 구현
piece = 0

for i in range(len(iron)):
    if iron[i] == "(":  # 여는 괄호
        iron_s.append("(")
    else:  # 닫는 괄호
        if iron[i-1] == "(":  # 레이저
            iron_s.pop()
            piece += len(iron_s)  # 스택 안 괄호 개수 추가
        else:  # 쇠막대기 끝
            iron_s.pop()
            piece += 1  # 쇠막대기 맨 마지막 조각 추가

print(piece)

