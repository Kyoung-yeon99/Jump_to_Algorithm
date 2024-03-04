from collections import deque
import sys
input = sys.stdin.readline

n = int(input())  # 2 ≤ N ≤ 100,000
m = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    m[a].append(b)
    m[b].append(a)

ans = [False]*(n+1)
# bfs
q = deque()
q.append(1)
while q:
    node = q.popleft()
    for nn in m[node]:
        if not ans[nn]:
            ans[nn] = node
            q.append(nn)

for i in ans[2:]:
    print(i)



