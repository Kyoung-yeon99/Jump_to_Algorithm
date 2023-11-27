n, m = map(int, input().split())
dna = [list(input()) for _ in range(n)]

ans1 = ''  # dna
ans2 = 0  # 개수

# dna
for i in range(m):
    # 사전순 정렬
    nucleo = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for j in range(n):
        value = dna[j][i]
        nucleo[value] += 1  # 개수 증가
    ans1 += max(nucleo, key=nucleo.get)  # 알파벳 최대값 찾기

# 개수
for x in range(n):
    for y in range(m):
        if ans1[y] != dna[x][y]:  # dna와 비교하면서 같지 않을 경우 hamming distance 하나 증가
            ans2 += 1
print(ans1)
print(ans2)
