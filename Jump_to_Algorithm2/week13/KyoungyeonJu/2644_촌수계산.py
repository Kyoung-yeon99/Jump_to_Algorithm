from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
family = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)


def bfs(a, b):
    q = deque()
    q.append(a)

    while q:
        n = q.popleft()
        if n == b:
            return visited[b]

        for i in family[n]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[n]+1

    return -1

print(bfs(a, b))