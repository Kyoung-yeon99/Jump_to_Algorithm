import sys
# 시간 초과 해결 방법
# 1. sys.stdin.readline()
# 2. insert 대신 배열 두개
stack_1 = list(sys.stdin.readline().rstrip())
stack_2 = []
m = int(input())
command = [
    list(map(str, sys.stdin.readline().split()))
    for _ in range(m)
]

for c in command:
    if c[0] == 'L' and stack_1:
        stack_2.append(stack_1.pop())
    elif c[0] == 'D' and stack_2:
        stack_1.append(stack_2.pop())
    elif c[0] == 'B' and stack_1:
        stack_1.pop()
    elif c[0] == 'P':
        stack_1.append(c[1])

print(''.join(stack_1 + list(reversed(stack_2))))


'''
# 시간 초과 

idx = len(s)
for c in command:
    if c[0] == 'L' and idx > 0:
        idx -= 1
    elif c[0] == 'D' and idx < len(s):
        idx += 1
    elif c[0] == 'B' and idx > 0:
        s.pop(idx -1)
        idx -= 1
    elif c[0] == 'P':
        s.insert(idx, c[1])
        idx += 1
print(''.join(s))
'''