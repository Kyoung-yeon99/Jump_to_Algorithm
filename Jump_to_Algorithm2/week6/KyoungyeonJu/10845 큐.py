from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()

for _ in range(n):
    c = list(input().split())  # c[0] 명령어 c[1] 정수, push만 c[1]이 있음
    if c[0] == 'push':
        q.append(c[1])
    elif c[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            f = q.popleft()
            print(f)
            q.appendleft(f)
    elif c[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            b = q.pop()
            print(b)
            q.append(b)




