n, m, x = map(int, input().split()) # 마을(학생) 수, 도로의 개수, 목적지
graph = [[] for _ in range(n+1)]
# i번째 도로의 시작점, 끝점, 소요시간
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

maxTime = 0
