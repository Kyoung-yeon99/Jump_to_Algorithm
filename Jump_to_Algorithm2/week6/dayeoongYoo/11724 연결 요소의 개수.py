# 무방향 그래프
# 연결요소 개수?

import sys

input = sys.stdin.readline  # n이 최댓값일 경우에 대비해 빠른 입력
# RecursionError 방지용
sys.setrecursionlimit(10 ** 8)


def dfs(now):  # 현재 노드
    for nxt in range(n):  # 다음 열
        if graph[now][nxt] and not chk[nxt]:  # 그래프로 갈 수 있고, 방문을 안 했을 경우
            chk[nxt] = True  # 방문 체크
            dfs(nxt)  # dfs 실행


n, m = map(int, input().split())
# 인접 행렬(N X N 2차원 리스트)
graph = [[0] * n for _ in range(n)]  # 0-based
# 간선
for _ in range(m):
    u, v = map(lambda x: x - 1, map(int, input().split()))  # 1-based to 0-based
    graph[u][v] = 1  # 간선으로 연결된 노드임.
    graph[v][u] = 1  # 무방향==양방향

# for i, row in enumerate(graph):
#     print(f'{i}: {row}')

ans = 0
# 방문 체크용
chk = [False] * n

for i in range(n):
    if not chk[i]:
        chk[i] = True
        ans += 1
        dfs(i)  # dfs
print(ans)
