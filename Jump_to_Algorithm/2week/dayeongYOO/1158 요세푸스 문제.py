# https://www.acmicpc.net/problem/1158

# 큐 이용

from collections import deque

N, K = map(int, input().split())
dq = deque()
for i in range(1, N + 1):
    dq.append(i)

print("<", end="")

ans = []
for _ in range(N):
    dq.rotate(-K + 1) # k번째 숫자는 로테이트하면 안됨(+1) 왼쪽 -> 오른쪽 이동
    ans.append(dq.popleft()) # 로테이트 후 k번째 요소 추가.

print(", ".join(map(str, ans)) + ">")
