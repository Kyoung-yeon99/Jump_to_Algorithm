# 수빈이가 있는 위치 N,  동생이 있는 위치 K
from collections import deque

n, k = map(int, input().split())
# 가장 빠른 시간을 구하기 위한 graph
graph = [0] * 100001
# 수빈이가 이동한 경로
chk = [0] * 100001


def move(curr_v):
    move_route = []
    now = curr_v
    for _ in range(graph[curr_v] + 1):  # 수빈이가 동생을 만날때까지 걸리는 시간 동안
        move_route.append(now)  # 현재 위치 추가
        now = chk[now]  # 이전 위치
    # 거꾸로 출력
    print(' '.join(map(str, move_route[::-1])))


def bfs():
    q = deque()
    q.append(n)
    while q:
        curr_v = q.popleft()

        if curr_v == k:  # 현재 노드가 동생이 있는 위치라면
            print(graph[curr_v])
            move(curr_v)  # 어떻게 이동?
            return

        for nxt_node in curr_v - 1, curr_v + 1, curr_v * 2:
            if 0 <= nxt_node <= 100000 and not graph[nxt_node]:  # 방문 하지 않았고, 범위 안의 수라면
                graph[nxt_node] = graph[curr_v] + 1
                q.append(nxt_node)
                # 수빈이가 지나온 경로를 알기위해 다음 위치에 현재 위치 기록
                chk[nxt_node] = curr_v


bfs()
