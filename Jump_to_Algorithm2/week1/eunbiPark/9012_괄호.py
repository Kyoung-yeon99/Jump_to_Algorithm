n = int(input())
for _ in range(n):
    string = input()
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else: # 괄호 없음
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')