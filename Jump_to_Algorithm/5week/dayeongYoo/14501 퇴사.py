n = int(input())
T = []
P = []
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

cache = [-1] * n


def dp(i):
    if i >= n:
        return 0

    if cache[i] == -1:
        # 일 안하고 그냥 넘어갈 경우
        cache[i] = dp(i + 1)

        # 일을 시작할 경우
        if i + T[i] <= n:
            cache[i] = max(cache[i], P[i] + dp(i + T[i]))

    return cache[i]


print(dp(0))
