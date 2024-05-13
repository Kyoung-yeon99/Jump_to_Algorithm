import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
graph = [[] for _ in range(n + 1)]
ans = 0
for _ in range(1, n):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 방향 그래프


def dfs(p, d):
    left, right = 0, 0
    for c, w in graph[p]:  # 자식이 있는 부모 노드의 경우
        tmp = dfs(c, w)
        if left <= right:  # 첫번째 자식은 왼쪽 자식이 되어야 함
            left = max(left, tmp)  # 왼쪽 자식에서 올라온 거리 갱신
        else:
            right = max(right, tmp)  # 오른쪽 자식에서 올라온 거리 갱신

    global ans
    ans = max(ans, left + right)  # 부모 노드에서의 최대 거리 갱신
    return max(left + d, right + d)  # 두 자식까지의 거리에 자기 자신 거리 더해서 반환


dfs(1, 0)
print(ans)
