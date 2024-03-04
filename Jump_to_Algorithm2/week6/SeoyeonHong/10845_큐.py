# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리
import sys
from collections import deque

input = sys.stdin.readline
N = int(input()) # 명령의 수
q = deque()
for _ in range(N):
    cmd = input().split() # 입력된 명령어
    if cmd[0] == "push":
        q.append(cmd[1]) # cmd[1] == 정수 X
    elif cmd[0] == "pop":
        print(q.popleft()) if len(q) != 0 else print(-1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        print(1) if len(q) == 0 else print(0)
    elif cmd[0] == "front":
        print(q[0]) if len(q) != 0 else print(-1)
    else: # back일 경우
        print(q[-1]) if len(q) != 0 else print(-1)




