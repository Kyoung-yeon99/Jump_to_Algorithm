tc = int(input())
for _ in range(tc):
    l, n = map(int, input().split())
    mint, maxt = 0, 0
    mid = l//2
    ant = [int(input()) for _ in range(n)]  # 개미 위치
    ant.append(mid)
    ant.sort()
    i = ant.index(mid)
    if i == 0:
        mint = l-ant[1]
    elif i == n:
        mint = ant[-2]
    else:
        mint = max(ant[i-1], l-ant[i+1])
    maxt = max(l-ant[0], ant[-1])
    print(mint, maxt)


