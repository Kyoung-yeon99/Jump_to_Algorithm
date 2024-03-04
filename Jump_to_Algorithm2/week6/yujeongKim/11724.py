import sys
sys.setrecursionlimit(10**6)
from collections import deque

n,m=map(int, sys.stdin.readline().split())

arr=[ [] for _ in range(n+1) ]

for _ in range(m):
    a,b=map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(node):
    visited[node]=True

    for i in arr[node]:
        if not visited[i]:
            dfs(i)

def bfs(node):
    queue = deque([node])
    visited[node]=True

    while queue:
        p = queue.popleft()

        for i in arr[p]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

cnt=0
visited=[False]*(n+1)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt+=1

print(cnt)