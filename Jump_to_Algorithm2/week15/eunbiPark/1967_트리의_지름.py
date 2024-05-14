import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))


def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for next, next_d in tree[cur]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[cur] + next_d
    m = max(visited)
    return [visited.index(m), m]

# 시작점에서 임의의 점 까지 가장 긴 거리를 구함
# 가장 먼 거리를 시작점으로 해서 다시 가장 긴 거리를 구함
print(bfs(bfs(1)[0])[1])