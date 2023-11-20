import heapq

# n명의 학생, m개의 단방향 도로, x 마을(파티)
n, m, x = map(int, input().split())
# 노드 간 정보를 인접리스트로 저장
# 연결된 마을 만들기
board = [[] for _ in range(n + 1)]

for _ in range(m):
    # s: 도로시작점, e: 도로 끝점, t: 필요한 시간
    s, e, t = map(int, input().split())
    board[s].append([e, t])  # 단방향

INF = 10000 * 1000  # m * n: 간선 x 노드 개수


#
def get_shortest_time(s, e):
    dist = [INF for _ in range(n + 1)]  # 경로 시간 초기화
    q = []
    heapq.heappush(q, [0, s])  # 시작 지점 넣어주기
    dist[s] = 0  # 시작지점 0으로 초기화
    while q:
        d, now = heapq.heappop(q)  # 현재까지 시간, 현재 마을 꺼내기
        if now == e:  # 도착지점이라면 시작에서 현재 ㅏㅁ을까지의 최단거리를 ㄱeturn
            return d
        if dist[now] < d:  # 현재 마을까지 걸리는 시간보다 꺼낸 시간이 더 크다면 pass
            continue
        for next in board[now]:  # 현재 마을에서 갈 수 있는 곳들 방문
            nd = next[1] + d  # 시간 더하기
            if nd < dist[next[0]]:  # 저장된 시간보다 더 작다면(최단경로)
                dist[next[0]] = nd
                heapq.heappush(q, [nd, next[0]])  # 그 마을로 이동
    return dist  # x에서 각 마을로 돌아갈때 시간을 list로 return


# 파티에서 마을까지 최단시간 구하기
p_to_v = get_shortest_time(x, 0)

# 답
ans = 0
for i in range(1, n + 1):
    # 왕복
    distance = get_shortest_time(i, x) + p_to_v[i]  # 왕복 길이
    ans = max(ans, distance)
print(ans)
