from collections import deque
t = int(input())
ps = []

for _ in range(t):  # 어차피 한 줄씩 결과를 낸다면 하나의 for문 사용 가능
    row = input()
    ps.append(list(map(str, row)))

for p in ps:
    s = deque()  # reset
    Flag = True  # reset
    for i in range(len(p)):
        if p[i] == "(":  # 여는 괄호이면
            s.append("(")
        else:  # 닫는 괄호이면
            if not s:  # 빈 스택이면
                print("NO")
                Flag = False
                break
            s.pop()

    if Flag:
        if not s:  # 스택이 비어 있으면 올바른 괄호 문자열
            print("YES")
        else:
            print("NO")




