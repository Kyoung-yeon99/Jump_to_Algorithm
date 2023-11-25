n, m , k = map(int, input().split()) # 도시의 수, 도로의 수, 포장할 도로의 수
ways = [[] for _ in range(n+1)]
for _ in range(m): # 도로가 연결하는 두 도시와 도로를 통과하는데 걸리는 시간
    c1, c2, t = map(int, input().split())
    ways[c1].append((c2, t))
    ways[c2].append((c1, t))

# 서울: 1번 도시, 포천: n번 도시
# 도로 포장 시 걸리는 시간 0