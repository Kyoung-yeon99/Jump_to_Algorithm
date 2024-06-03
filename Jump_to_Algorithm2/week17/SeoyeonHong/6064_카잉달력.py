# <M:N>이 카잉 달력의 마지막 해라고 하면 <x:y>는 몇 번째 해를 나타내는지 구하는 프로그램
# 시간초과
def lcm(a, b):
    for i in range(max(a, b), (a * b)+1):
        if i % a == 0 and i % b == 0:
            return i

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    if M > N:
        M, N, x, y = N, M, y, x
    k = 1 
    expressible = False
    if x == y:
        print(x)
    else:
        last_year = lcm(M, N) # M과 N의 최소공배수

        if x == M:
            for k in range(y, last_year+1, N):
                if k % M == 0:
                    expressible = True
                    print(k)
                    break
        elif y == N:
            for k in range(x, last_year+1, M):
                if k % N == 0:
                    expressible = True
                    print(k)
                    break
        else: 
            for k in range(x, last_year+1, M):
                if k % N == y:
                    expressible = True
                    print(k)
                    break

        if not expressible:
            print(-1)