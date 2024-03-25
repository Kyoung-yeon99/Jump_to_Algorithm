# 스타트 팀과 링크 팀의 능력치 차이의 최솟값
import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
S = []
min_diff = 20000 # 능력치 차이의 최솟값
total = 0
for _ in range(N):
    row = list(map(int, input().split()))
    total += sum(row)
    S.append(row)

# N명 중 N//2명으로 팀을 구성하는 모든 경우에 대하여(중복 조합 제외)
member_num = N // 2
comb = list(combinations([i for i in range(N)], member_num)) # 가능한 모든 조합
comb_num = len(comb) // 2 # 중복을 제외한 조합의 개수

for k in range(comb_num):
    sumA = 0 # 팀A의 능력치 합
    sumB = 0 # 팀B의 능력치 합
    m = comb[k] 
    for i in range(member_num - 1):
        for j in range(i + 1, member_num):
            sumA += S[m[i]][m[j]] + S[m[j]][m[i]]
    m = comb[-k-1]
    for i in range(member_num - 1):
        for j in range(i + 1, member_num):
            sumB += S[m[i]][m[j]] + S[m[j]][m[i]]
    min_diff = min(min_diff, abs(sumA - sumB)) # 차이의 최솟값 갱신

print(min_diff)

