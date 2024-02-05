n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

# 플로이드-워셜: 거쳐 가는 노드 i 기준
for i in range(n):
    for a in range(n):
        for b in range(n):
            if m[a][i] and m[i][b]:  # a에서 i를 거쳐 b, 모두 값이 1이면
                m[a][b] = 1

for row in m:
    print(*row)
