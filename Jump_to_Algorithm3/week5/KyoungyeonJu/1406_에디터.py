# L 왼쪽(0이면 무시)
# D 오른쪽(l+1이면 무시)
# B 커서 왼쪽 문자 삭제(0이면 무시)
# P $ - $라는 문자를 커서 왼쪽에 추가
import sys
input = sys.stdin.readline

chars = list(input().rstrip())
out = []
n = int(input().rstrip())

for i in range(n):
    command = input().rstrip()
    if command == 'L':
        if chars:
            out.append(chars.pop())
    elif command == 'D':
        if out:
            chars.append(out.pop())
    elif command == 'B':
        if chars:
            chars.pop()
    else:
        _, c = command.split()
        chars.append(c)

print(''.join(chars)+''.join(out[::-1]))


