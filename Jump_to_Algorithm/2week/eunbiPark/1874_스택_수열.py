n = int(input())
stack = []
answer = []
flag = 0
cur = 1

for i in range(n):
    num = int(input())
    while cur <= num: # 입력한 수 만날 때 까지 push
        stack.append(cur)
        answer.append('+')
        cur += 1

    if stack[-1] == num: # 꺼낼 수 있다면 (마지막 append 값 == num)
        stack.pop()
        answer.append('-')
    # 해당 숫자까지 append 했는데 가장 위에 있는 값이 num과 다르다면
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for a in answer:
        print(a)