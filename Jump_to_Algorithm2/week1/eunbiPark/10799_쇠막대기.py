import sys
input = sys.stdin.readline

s = list(input().strip())
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:
        if s[i-1] == '(': # 레이저 판단
            stack.pop()
            cnt += len(stack) # 저장한 열린 괄호 개수

        else: # 레이저가 아니라면
            stack.pop()
            cnt += 1
print(cnt)