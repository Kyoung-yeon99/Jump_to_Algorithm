# 입력부
# n개 도시, m개의 도로 수, k개 포장할 도로 수
import heapq

n, m, k = map(int, input().split())
# 인접리스트
board = [[] for _ in range(n + 1)]
# 양방향 리스트
for _ in range(m):
    # M개의 줄에 대해 도로가 연결하는 두 도시(a, b), 도로를 통과하는데 걸리는 시간
    a, b, time = map(int, input().split())
    board[a].append((b, time))
    board[b].append((a, time))

# 무한대 설정
INF = float('inf')

# dis: 2차원 다익스트라 배열. 현재 정점 i에서 도로 포장을 j개 했을 경우의 최소거리
dist = [[INF] * (k + 1) for _ in range(n + 1)]
q = []
for i in range(k + 1):
    dist[1][i] = 0
heapq.heappush(q, (0, 1, 0))

# 다익스트라
while q:
    now_dist, now, p = heapq.heappop(q)

    if dist[now][p] < now_dist:
        continue
    # 현재 정점에서 도로 포장 가능할 경우
    if p + 1 <= k:
        for (nxt, next_dist) in board[now]:
            if dist[nxt][p + 1] > now_dist:
                dist[nxt][p + 1] = now_dist  # 갱신
                heapq.heappush(q, (now_dist, nxt, p + 1))
    # 도로 포장을 하지 않는 경우
    for (nxt, next_dist) in board[now]:
        if dist[nxt][p] > now_dist + next_dist:
            dist[nxt][p] = now_dist + next_dist
            heapq.heappush(q, (now_dist + next_dist, nxt, p))
# 출력부
ans = INF
for i in range(k + 1):
    ans = min(ans, dist[n][i])
print(ans)
