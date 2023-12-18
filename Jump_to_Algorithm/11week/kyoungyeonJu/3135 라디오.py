a, b = map(int, input().split())
n = int(input())
fav = [int(input()) for _ in range(n)]
diff = abs(a-b)  # a와 b 주파수 차이
cnt = 0
is_change = False

for i in range(n):
    if abs(fav[i]-b) < diff:
        a = fav[i]
        diff = abs(fav[i]-b)
        is_change = True

if is_change:
    cnt += 1

print(cnt+abs(a-b))
