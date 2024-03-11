# https://wikidocs.net/206356
# bfs를 돌면서 구한 케빈 베이컨의 수가 최소인 사람을 찾습니다.
# min_total에는 최소 케빈 베이컨 수를 저장하기 위해서 무한대의 값으로 초기화 합니다.
# 반복문을 통해 각 사람들의 케빈 베이컨 수를 구합니다. 그리고 min_total값과 비교하면서 최소값을 min_total에 저장합니다.
# 우리는 최소의 케빈 베이컨 수를 구하는 것이 아니라 최소의 케빈 베이컨 수를 가진 사람을 찾는 것이기 때문에 ans값에 최소값을 가진 사람을 저장합니다.
# 마지막으로 최소값이 저장된 사람을 출력

from collections import deque

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v) # 친구관계는 양방향
    arr[v].append(u)


def bfs(start):
    visited = [-1] * (n + 1)

    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        node = q.popleft()

        for next_node in arr[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                q.append(next_node)
    total = sum(visited)
    return total


min_total = float("INF")
ans = 0
for i in range(1, n + 1):

    total = bfs(i)
    if total < min_total:
        min_total = total
        ans = i

print(ans)
