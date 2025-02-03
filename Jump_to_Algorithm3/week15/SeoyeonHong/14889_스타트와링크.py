import sys
from itertools import combinations
import math

input = sys.stdin.readline
N = int(input())
S = [] # 능력치
min_diff = int(1e9) # 능력치 차이의 최솟값

for _ in range(N):
    S.append(list(map(int, input().split())))

comb_count = math.comb(N, N//2) # 조합의 개수
comb = list(combinations(range(N), N//2)) # N//2명을 뽑는 조합
teamA = comb[:comb_count//2]
teamB = comb[comb_count//2:][::-1]

for t in range(comb_count//2):
    a, b = 0, 0 # A팀과 B팀의 능력치 총합

    for i, j in combinations(teamA[t], 2):
        a += S[i][j] + S[j][i]
    
    for i, j in combinations(teamB[t], 2):
        b += S[i][j] + S[j][i]

    min_diff = min(min_diff, abs(a - b)) # 능력치의 차이 최솟값 갱신

    if min_diff == 0:
        break

print(min_diff)