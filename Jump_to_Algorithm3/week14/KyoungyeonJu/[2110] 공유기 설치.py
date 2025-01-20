import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()
min_d = 1
max_d = houses[n-1] - houses[0]

while min_d <= max_d:
    mid_d = (min_d+max_d)//2
    cnt = 1
    last = houses[0]
    for i in range(1, n):
        if houses[i] - last >= mid_d:
            cnt += 1
            last = houses[i]

    if cnt >= c:
        min_d = mid_d + 1
    else:
        max_d = mid_d - 1

print(min_d-1)