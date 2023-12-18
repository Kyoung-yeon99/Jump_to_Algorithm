import sys

m, n = map(int, sys.stdin.readline().split()) # 격자칸 크기, 날짜 수
growth = [1 for _ in range(2*m-1)]

for _ in range(n): # 가장 위쪽 & 같은 열의 애벌레의 총 성장값
    zero, one, two = map(int, sys.stdin.readline().split())
    for i in range(zero, zero+one):
        growth[i] += 1
    for i in range(zero+one, 2*m-1):
        growth[i] += 2

larva = [[1 for _ in range(m)] for _ in range(m)]

for r in range(m):
    for c in range(m):
        if c == 0:
            print(growth[m - r - 1], end = ' ')
        else:
            print(growth[m + c - 1], end = ' ') # 가장 위쪽 & 같은 열의 애벌레 성장값이 최대
    print()