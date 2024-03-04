# 큐 만들기
# 파이썬에서 큐를 만들때는 deque 사용
# 간편하게 deque 메소드 이용하면 되지 않을까?
import sys
from collections import deque

q = deque()

# 명령어가 6가지이니까 경우 많음(switch 이용 -> python switch 문 어캐썼더라. 반전 없다네(if~elif문 사용)
# command = ["push", "pop", "size", "empty", "front", "back"]

# 시간초과로 input 대신 sys.stdin.readline 쓰자.

# n = int(input())
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    c = command[0]

    if c == "push":
        q.append(command[1])
    elif c == "pop":
        if len(q) == 0:  # 가장 앞에 있는 정수 빼기.
            print(-1)
        else:
            print(q.popleft())  # popleft()는 큐의 왼쪽(첫 번째)에서 원소를 제거
    elif c == "size":
        print(len(q))
    elif c == "empty":
        print(1 if len(q) == 0 else 0)

    elif c == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif c == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])  # pop()은 큐의 오른쪽(마지막)에서 원소를 제거
