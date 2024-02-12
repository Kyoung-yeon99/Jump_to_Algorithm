import sys

input = sys.stdin.readline


def dfs(n):
    global ans

    if n == N:  # 끝까지 도달
        ans += 1
        return
    for j in range(N):
        if v1[j] == v2[n + j] == v3[n - j] == 0:
            v1[j] = v2[n + j] = v3[n - j] = 1  # 퀸 두기
            dfs(n + 1)
            v1[j] = v2[n + j] = v3[n - j] = 0  # 해제


N = int(input())
# 체스판
v1 = [0] * N
v2 = [0] * (N * 2)
v3 = [0] * (N * 2)

ans = 0
dfs(0)
print(ans)
