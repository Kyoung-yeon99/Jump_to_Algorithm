import sys
input = sys.stdin.readline
n = int(input().rstrip())
s = set()

for _ in range(n):
    command = list(input().rstrip().split())
    c = command[0]
    if len(command) == 2:
        x = command[1]

    if c == 'add':
        if x not in s:
            s.add(x)
    elif c == 'remove':
        if x in s:
            s.remove(x)
    elif c == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    elif c == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif c == 'all':
        s = set(str(i) for i in range(1, 21))
    elif c == 'empty':
        s.clear()