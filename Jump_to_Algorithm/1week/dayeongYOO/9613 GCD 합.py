import sys

input = sys.stdin.readline

n = int(input())


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


for _ in range(n):
    tc = list(map(int, input().split()))
    ans = 0
    for i in range(1, tc[0]):  # 수의 개수
        for j in range(i + 1, tc[0] + 1):  # 두 수를 짝지어 준다.
            ans += gcd(tc[i], tc[j])

    print(ans)
