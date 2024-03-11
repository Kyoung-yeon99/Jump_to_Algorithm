import sys

input = sys.stdin.readline
N, M = map(int, input().split()) # 유저의 수, 친구 관계의 수
INF = int(1e9) # 가능한 케빈 베이컨의 수보다 큰 수
fr = [[INF for _ in range(N+1)] for _ in range(N+1)] # 친구 관계
kb = INF # 케빈 베이컨의 수
ans = 0 # 케빈 베이컨의 수가 가장 작은 사람

for _ in range(M):
    A, B = map(int, input().split())
    fr[A][B] = 1
    fr[B][A] = 1

for i in range(1, N+1):
    fr[i][i] = 0

# 플로이드 워셜 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            fr[i][j] = min(fr[i][j], fr[i][k] + fr[k][j])
    
# 케빈 베이컨 수가 가장 작은 사람 중 번호가 가장 작은 사람
for i in range(1, N+1):
    s = sum(fr[i][1:])
    if kb > s:
        kb = s
        ans = i

print(ans)
        