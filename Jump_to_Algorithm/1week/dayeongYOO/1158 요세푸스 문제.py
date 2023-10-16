# 큐 이용

from collections import deque

N, K = map(int, input().split())
dq = deque()
for i in range(1, N + 1):
    dq.append(i)

print("<", end="")

ans = []
for _ in range(N):
    dq.rotate(-K + 1)
    ans.append(dq.popleft())

print(", ".join(map(str, ans)) + ">")
