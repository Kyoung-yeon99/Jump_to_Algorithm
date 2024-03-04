import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
q = []
graph = [[] for _ in range(n + 1)]
inDegree = [0 for _ in range(n + 1)]
ans = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, n + 1):
    if inDegree[i] == 0:
        heapq.heappush(q, i)

while q:
    tmp = heapq.heappop(q)
    ans.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(q, i)

print(' '.join(map(str, ans)))