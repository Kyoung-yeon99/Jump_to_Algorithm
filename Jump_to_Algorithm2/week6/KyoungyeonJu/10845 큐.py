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
        if len(q) == 0:  # 비어있는지 확인
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
        if len(q) == 0:  # 비어있는지 확인
            print(-1)
        else:
            f = q.popleft()  # 빼고
            print(f)  # 출력하고
            q.appendleft(f)  # 다시 넣고
    elif c[0] == 'back':
        if len(q) == 0:  # 비어있는지 확인
            print(-1)
        else:
            b = q.pop()  # 빼고
            print(b)  # 출력하고
            q.append(b)  # 다시 넣고




