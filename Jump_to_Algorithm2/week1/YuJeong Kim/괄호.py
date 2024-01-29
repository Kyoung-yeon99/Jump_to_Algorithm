n=int(input())

for _ in range(n):
    _input = input()
    stack=[]
    flag=True

    for ch in _input:
        if ch=='(':
            stack.append('(')
        elif ch==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                flag=False

    if stack:
        flag=False

    if flag:
        print("YES")
    else:
        print("NO")
