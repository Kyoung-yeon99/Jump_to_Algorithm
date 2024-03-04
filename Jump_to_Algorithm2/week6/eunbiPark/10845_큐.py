import sys
n = int(input())
# commands = []
ret = []
idx  = -1
for _ in range(n):
    # commands.append(sys.stdin.readline().split())
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        ret.append(int(command[1]))
        idx += 1
    elif command[0] == 'pop':
        if idx == -1:
            print(-1)
        else:
            idx -= 1
            print(ret.pop(0))
    elif command[0] == 'size':
        print(idx + 1)
    elif command[0] == 'empty':
        if idx == -1:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if idx == -1:
            print(-1)
        else:
            print(ret[0])
    elif command[0] == 'back':
        if idx == -1:
            print(-1)
        else:
            print(ret[-1])