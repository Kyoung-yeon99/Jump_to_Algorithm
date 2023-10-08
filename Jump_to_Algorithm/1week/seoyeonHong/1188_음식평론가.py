n, m = map(int, input().split())
c = 0
for i in range(1, m * n):
    if i % m == 0 and i % n == 0:
        c += 1
print(m - 1 - c)