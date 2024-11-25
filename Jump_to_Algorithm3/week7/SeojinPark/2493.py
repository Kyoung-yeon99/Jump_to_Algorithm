n=int(input())
top = list(map(int,input().split()))
stack=[]
res=[]

for i in range(n):
    while stack and top[stack[-1]]<top[i]:
        stack.pop()

    # 스택이 비어 있으면
    if not stack:
        res.append(0)
    else:
        res.append(stack[-1]+1)
    # 현재 탑의 인덱스를 스택에 추가
    stack.append(i)
print(*res)



