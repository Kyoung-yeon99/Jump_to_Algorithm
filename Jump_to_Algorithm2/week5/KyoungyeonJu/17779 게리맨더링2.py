import sys
input = sys.stdin.readline


def calculate(d1, d2, x, y):
    global maps, total, diff, n
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0

    # 1번 선거구 1 ≤ r < x+d1, 1 ≤ c ≤ y
    c1 = y
    for r in range(x+d1-1):
        if r >= x-1:
            c1 -= 1
        sum1 += sum(maps[r][:c1])

    # 2번 선거구 1 ≤ r ≤ x+d2, y < c ≤ N
    c2 = y
    for r in range(x+d2):
        if r > x-1:
            c2 += 1
        sum2 += sum(maps[r][c2:])

    # 3번 선거구  x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    c3 = y-d1-1
    for r in range(x+d1-1, n):
        sum3 += sum(maps[r][:c3])
        if r < x+d1+d2-1:
            c3 += 1

    # 4번 선거구 x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    c4 = (y+d2)-n-1
    for r in range(x+d2, n):
        sum4 += sum(maps[r][c4:])
        if r <= x+d1+d2-1:
            c4 -= 1

    # 5번 선거구
    sum5 = total - (sum1+sum2+sum3+sum4)

    diff = min(diff, max(sum1, sum2, sum3, sum4, sum5) - min(sum1, sum2, sum3, sum4, sum5))


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
diff = int(1e9)
total = 0
for i in range(n):
    total += sum(maps[i])

# d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N
for d1 in range(1, n-1):  # 1부터 n-2까지
    for d2 in range(1, n-1):  # 1부터 n-2까지
        for x in range(1, n-d1-d2+1):  # 1부터 n - (d1+d2)까지
            for y in range(1+d1, n-d2+1):  # 1+d1부터 n-d2까지
                if x+d1+d2 <= n and y+d2 <= n:
                    calculate(d1, d2, x, y)

print(diff)
