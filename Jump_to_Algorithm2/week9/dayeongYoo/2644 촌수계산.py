# bfs
from collections import deque
# 사람들 n
n = int(input())
# 촌수 계산할 두 사람
p1, p2 = map(int, input().split())
# 부모-자식들 간 관계 개수 m
m = int(input())

# 부모-자식들 간 관계 저장할 그래프
graph = [[] for _ in range(n + 1)]
# 중복 방지
visited = [False] * (n + 1)

# 부모 자식간 관계 나타내는 두 번호 x,y
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(v, target):
    count = 0
    q = deque([[v, count]])
    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if v == target:
            return count

        if not visited[v]:
            count += 1
            visited[v] = True
            for i in graph[v]:
                if not visited[i]:
                    q.append([i, count])
    return -1


print(bfs(p1, p2))
