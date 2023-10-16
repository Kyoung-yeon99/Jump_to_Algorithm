import sys

left = list(sys.stdin.readline().rstrip()) # 커서의 왼쪽에 있는 문자들(초기 문자열)
right = [] # 커서의 오른쪽에 있는 문자들
m = int(input()) # 명령어 개수

for _ in range(m):
    command = sys.stdin.readline().split() # input(), insert() 쓸 경우 시간 초과
    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(command[1])

left.extend(reversed(right))
print(''.join(left))