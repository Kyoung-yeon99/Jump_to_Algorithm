# https://www.acmicpc.net/problem/5430
from collections import deque

tc = int(input())
for t in range(tc):
    command = input()
    k = int(input())
    q = deque(input()[1:-1].split(','))  # ','를 기준으로 자른다.

    flag = 0

    if k == 0:
        q = []
    for c in command:
        if c == 'R':
            flag += 1
        elif c == 'D':
            if len(q) == 0:
                print('error')
                break
            else:
                if flag % 2 == 1:
                    q.pop()
                else:
                    q.popleft()
    else:
        if flag % 2 == 1:
            q.reverse()
        print('[' + ','.join(q) + ']')
