# fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램
T = int(input())
f = [(1, 0), (0, 1), (1, 1), (1, 2)]
n = 3
for _ in range(T):
    N = int(input())
    if N < n:
        print(*f[N])
    else:
        for i in range(n+1, N+1):
            f.append((f[i-1][0] + f[i-2][0], f[i-1][1] + f[i-2][1]))
        print(*f[N])
        n = N

