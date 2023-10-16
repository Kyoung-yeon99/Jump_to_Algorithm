n = int(input())
cur = 1
stack = [] # 스택
operation = [] # 연산 저장 변수

for i in range(n):
    k = int(input())
    
    for j in range(cur, k+1): # k를 꺼내기 위해서 K를 스택에 push
        operation.append('+')
        stack.append(j)
        cur += 1
        
    if k != stack.pop(): # push 이후 pop을 실행했을 때 k가 아닌 수가 나올 경우 불가능
        print("NO")
        break
    operation.append('-') # k를 꺼내기 위해 스택에서 pop
    
if len(stack) == 0:
    for o in operation:
        print(o)