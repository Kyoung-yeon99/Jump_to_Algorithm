# 입력
import heapq

n, e = map(int, input().split())  # 정점 개수(node), 간선 개수(edge)
start_v = int(input())  # 시작 정점의 번호

# 노드 간 정보를 인접리스트로 저장
board = [[] for _ in range(n + 1)]

for _ in range(e):
    u, v, w = map(int, input().split())  # u->v로 가는 가중치 w인 간선
    board[u].append((v, w))  # 다음 노드, 가중치 저장

INF = 10000000  # (간선 가중치의 최댓값) * (정점 개수 - 1) 보다 큰 값을 사용

# 시작점과 모든 지점과의 거리 정보 리스트
dist = [INF for _ in range(n + 1)]
dist[start_v] = 0  # 시작노드는 최소거리가 0이다

q = []  # 노드 저장할 큐
# 우선순위 큐 이용
# 시작 정점에서 거리가 가장 가까운 것들만 우선적으로 뽑아 쓰기 위해.
heapq.heappush(q, (0, start_v))  # (거리, bfs 수행 정점) 순으로

while q:
    # short: 현재 노드까지의 최소거리, now: 현재 노드
    short, now = heapq.heappop(q)
    # 연결된 노드를 꺼내서, 노드와 현재 노드와의 거리 가져온다
    for next, dis in board[now]:
        # 현재까지의 최소 거리 + 두 노드 사이 거리 vs dist의 시작부터 현재 노드까지의 거리 비교
        if short + dis < dist[next]:
            dist[next] = short + dis
            # 갱신 후, 가장 최소 거리의 노드부터 q에 넣어 다시 꺼낸다.
            heapq.heappush(q, (short + dis, next))

for i in range(1, n + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
