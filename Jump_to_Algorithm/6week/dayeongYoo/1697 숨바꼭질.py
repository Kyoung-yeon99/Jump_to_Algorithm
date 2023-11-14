# 수빈이가 있는 위치 N,  동생이 있는 위치 K
from collections import deque

n, k = map(int, input().split())
# 가장 빠른 시간을 구하기 위한 graph
graph = [0] * 100001


def bfs():
    q = deque()  # 큐 생성
    q.append(n)  # 수빈이의 위치를 삽입(첫번째 요소)

    while q:
        curr_v = q.popleft()  # 현재 위치

        if curr_v == k:  # 현재 노드가 동생이 있는 위치라면
            print(graph[curr_v])
            break # 탈출

        for nx in curr_v - 1, curr_v + 1, curr_v * 2:  # 다음 노드 탐색(걷거나+-1, 순간이동 *2)
            # 다음 노드가 방문 하지 않았고, 범위 안의 수라면
            if 0 <= nx <= 100000 and not graph[nx]:
                # 최단 거리 갱신(방문 체크)
                graph[nx] = graph[curr_v] + 1
                q.append(nx)


bfs()
