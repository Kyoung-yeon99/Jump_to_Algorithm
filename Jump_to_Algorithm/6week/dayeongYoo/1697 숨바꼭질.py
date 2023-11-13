# 수빈이가 있는 위치 N,  동생이 있는 위치 K
from collections import deque

n, k = map(int, input().split())
# 가장 빠른 시간을 구하기 위한 graph
graph = [0] * 100001


def bfs():
    q = deque()
    q.append(n)
    while q:
        curr_v = q.popleft()

        if curr_v == k:  # 현재 노드가 동생이 있는 위치라면
            print(graph[curr_v])

        for i in curr_v - 1, curr_v + 1, curr_v * 2:
            if 0 <= i <= 100000 and not graph[i]:  # 방문 하지 않았고, 범위 안의 수라면
                graph[i] = graph[curr_v] + 1
                q.append(i)


bfs()
