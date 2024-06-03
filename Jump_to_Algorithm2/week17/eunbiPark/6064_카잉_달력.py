import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())

    k = x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0: # 문제 조건
            print(k)
            break
        # k = x 이거나 k = x+m or x+2m...
        k += m # 1씩 더하는 것이 아니라 m씩 점프
    else:
        print(-1)