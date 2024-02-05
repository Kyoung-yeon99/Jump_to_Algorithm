n = int(input())
coord = [list(map(int, input().split())) for _ in range(n)]

# 우선순위 1. y좌표 기준 오름차순 정렬 2. 같으면 x좌표
coord.sort(key=lambda s: (s[1], s[0]))

for c in coord:
    print(c[0], c[1])
