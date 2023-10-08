import sys

input = sys.stdin.readline

n = int(input())
ans = 0  # 개수

while (n >= 0):
    if n % 5 == 0:
        ans += (n // 5)
        print(ans)
        break
    n -= 3  # 5의 배수가 아니라면 3을 빼준다.
    ans += 1
else:
    print(-1)
