# https://www.acmicpc.net/problem/1874

count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num 이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num과 스택 맨 위 숫자가 동일하다면 제거한다.
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 탈출
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)
