from collections import deque

n = int(input())

stack = deque()
result = list()  # 연산자 결과 저장 리스트

top = 1

for i in range(n):
    num = int(input())

    while top <= num:
        stack.append(top)
        result.append('+')
        top += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit()


result = "\n".join(result)
print(result)


